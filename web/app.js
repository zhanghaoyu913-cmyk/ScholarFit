const STORAGE_KEY = "scholarfit.responses.v1";
const params = new URLSearchParams(window.location.search);
const appMode = params.get("mode") === "full" ? "full" : "quick";
const QUICK_ITEM_IDS = new Set([
  "CH1_SJT_001",
  "CH1_SJT_003",
  "CH1_BEHAVIOR_001",
  "CH2_SJT_001",
  "CH2_RANK_001",
  "CH2_SJT_003",
  "CH3_SJT_001",
  "CH3_RANK_001",
  "CH3_BEHAVIOR_001",
  "CH4_SJT_001",
  "CH4_SJT_004",
  "CH4_SLIDER_002",
  "CH5_SJT_001",
  "CH5_SJT_003",
  "CH6_SJT_001",
  "CH6_SJT_004",
  "CH7_SJT_001",
  "CH7_SJT_004",
  "CH8_SJT_001",
  "CH8_REFLECT_001",
]);

const PROFILE_PREFIXES = {
  motivation: "科研动机",
  research_self_efficacy: "科研自我效能",
  research_behavior: "科研行为证据",
  personality: "人格与科研风格",
  conscientiousness: "人格与科研风格",
  emotional_stability: "人格与科研风格",
  agreeableness: "人格与科研风格",
  direction_interest: "研究方向匹配",
  advisor_fit: "导师/实验室匹配",
  help_seeking: "导师/实验室匹配",
  stress_recovery: "压力恢复",
  academic_integrity: "学术诚信",
  research_maturity: "成长建议信号",
  growth: "成长建议信号",
};

const PROFILE_ORDER = [
  "科研动机",
  "科研自我效能",
  "科研行为证据",
  "人格与科研风格",
  "研究方向匹配",
  "导师/实验室匹配",
  "压力恢复",
  "学术诚信",
  "成长建议信号",
  "其他信号",
];

const MODE_LABEL = appMode === "full" ? "完整版" : "快速版";
const MODE_DESCRIPTION = appMode === "full" ? "80 题，适合完整自我梳理。" : "20 题，适合首次体验和快速分享。";

const sourceChapters = window.SCHOLARFIT_ITEM_BANK || [];
const chapters = sourceChapters
  .map((chapter) => ({
    ...chapter,
    items: appMode === "full" ? chapter.items || [] : (chapter.items || []).filter((item) => QUICK_ITEM_IDS.has(item.id)),
  }))
  .filter((chapter) => chapter.items.length);
const allItems = chapters.flatMap((chapter) => chapter.items || []);

let activeChapter = "all";
let currentIndex = 0;
let responses = loadResponses();
let latestMarkdown = "";

const el = {
  chapterNav: document.querySelector("#chapterNav"),
  progressText: document.querySelector("#progressText"),
  chapterText: document.querySelector("#chapterText"),
  progressBar: document.querySelector("#progressBar"),
  itemStage: document.querySelector("#itemStage"),
  reportPanel: document.querySelector("#reportPanel"),
  prevButton: document.querySelector("#prevButton"),
  nextButton: document.querySelector("#nextButton"),
  showReportButton: document.querySelector("#showReportButton"),
  clearButton: document.querySelector("#clearButton"),
  modeTitle: document.querySelector("#modeTitle"),
  modeDescription: document.querySelector("#modeDescription"),
  modeText: document.querySelector("#modeText"),
};

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function loadResponses() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveResponses() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(responses));
  renderProgress();
}

function visibleItems() {
  if (activeChapter === "all") return allItems;
  return allItems.filter((item) => item.id.startsWith(`CH${activeChapter}_`));
}

function hasResponse(item) {
  const response = responses[item.id];
  if (response === undefined || response === null) return false;
  if (Array.isArray(response)) return response.length > 0;
  if (typeof response === "string") return response.trim().length > 0;
  return true;
}

function renderChapters() {
  const allActive = activeChapter === "all" ? "active" : "";
  const buttons = [
    `<button class="chapter-button ${allActive}" data-chapter="all" type="button"><span>${MODE_LABEL}全部题目</span><strong>${answeredCount(allItems)}/${allItems.length}</strong></button>`,
    ...chapters.map((chapter) => {
      const items = chapter.items || [];
      const active = String(chapter.chapter_id) === String(activeChapter) ? "active" : "";
      return `<button class="chapter-button ${active}" data-chapter="${chapter.chapter_id}" type="button"><span>${escapeHtml(chapter.chapter)}</span><strong>${answeredCount(items)}/${items.length}</strong></button>`;
    }),
  ];
  el.chapterNav.innerHTML = buttons.join("");
  el.chapterNav.querySelectorAll("[data-chapter]").forEach((button) => {
    button.addEventListener("click", () => {
      activeChapter = button.dataset.chapter;
      currentIndex = 0;
      el.reportPanel.classList.add("hidden");
      renderChapters();
      renderItem();
      renderProgress();
    });
  });
}

function answeredCount(items) {
  return items.filter(hasResponse).length;
}

function renderProgress() {
  const answered = answeredCount(allItems);
  const percent = allItems.length ? (answered / allItems.length) * 100 : 0;
  el.progressText.textContent = `${answered} / ${allItems.length}`;
  el.progressBar.style.width = `${percent}%`;
  if (activeChapter === "all") {
    el.chapterText.textContent = `${MODE_LABEL}全部题目`;
  } else {
    const chapter = chapters.find((entry) => String(entry.chapter_id) === String(activeChapter));
    el.chapterText.textContent = chapter ? chapter.chapter : "当前章节";
  }
}

function renderItem() {
  const items = visibleItems();
  if (!items.length) {
    el.itemStage.innerHTML = `<div class="item-card"><h3>没有可用题目</h3></div>`;
    return;
  }
  currentIndex = Math.max(0, Math.min(currentIndex, items.length - 1));
  const item = items[currentIndex];
  el.itemStage.innerHTML = `
    <article class="item-card">
      <div class="item-meta">
        <span class="pill">${escapeHtml(item.id)}</span>
        <span class="pill">${escapeHtml(item.chapter)}</span>
        <span class="pill">${typeLabel(item.type)}</span>
        <span class="pill">${currentIndex + 1} / ${items.length}</span>
      </div>
      <h3>${escapeHtml(item.chapter)}</h3>
      <div class="scenario">${escapeHtml(item.scenario)}</div>
      <div class="question">${escapeHtml(item.question)}</div>
      ${renderAnswerControl(item)}
      <p class="muted">${escapeHtml(item.reporting_rule || "仅解释行为倾向，不做淘汰或诊断。")}</p>
    </article>
  `;
  bindAnswerControl(item);
  el.prevButton.disabled = currentIndex === 0;
  el.nextButton.textContent = currentIndex === items.length - 1 ? "本章完成，生成报告" : "下一题";
}

function typeLabel(type) {
  return {
    situational_judgment: "情境判断",
    ranking: "排序题",
    slider: "滑条题",
    reflection: "微反思",
    behavior_evidence: "行为证据",
  }[type] || type;
}

function renderAnswerControl(item) {
  if (item.type === "situational_judgment") return renderOptions(item);
  if (item.type === "ranking") return renderRanking(item);
  if (item.type === "slider") return renderSlider(item);
  if (item.type === "reflection") return renderReflection(item);
  if (item.type === "behavior_evidence") return renderBehaviorEvidence(item);
  return `<p class="muted">暂不支持该题型。</p>`;
}

function renderOptions(item) {
  const current = responses[item.id];
  return `<div class="option-grid">${Object.entries(item.options || {})
    .map(([key, text]) => {
      const selected = current === key ? "selected" : "";
      return `<button class="option-card ${selected}" data-option="${key}" type="button"><span class="option-key">${key}</span><span>${escapeHtml(text)}</span></button>`;
    })
    .join("")}</div>`;
}

function renderRanking(item) {
  const optionKeys = Object.keys(item.options || {});
  const order = Array.isArray(responses[item.id]) && responses[item.id].length ? responses[item.id] : optionKeys;
  return `
    <div class="ranking-list">
      ${order
        .map(
          (key, index) => `
            <div class="rank-row" data-rank-key="${key}">
              <div><strong>${key}.</strong> ${escapeHtml(item.options[key])}</div>
              <div class="rank-actions">
                <button class="small-button" data-rank-move="${index}" data-direction="-1" type="button">上移</button>
                <button class="small-button" data-rank-move="${index}" data-direction="1" type="button">下移</button>
              </div>
            </div>
          `,
        )
        .join("")}
    </div>
    <button class="ghost-button" data-rank-confirm="true" type="button">确认当前排序</button>
    <p class="muted">调整顺序后会自动保存。当前位置越靠前，代表越可能优先采取；如果默认顺序正好符合你，也可以直接确认。</p>
  `;
}

function renderSlider(item) {
  const value = responses[item.id] ?? 3;
  return `
    <div class="slider-wrap">
      <input id="sliderInput" type="range" min="${item.scale?.min || 1}" max="${item.scale?.max || 5}" step="1" value="${value}" />
      <div class="slider-labels">
        <span>${escapeHtml(item.scale?.left_label || "左侧")}</span>
        <strong id="sliderValue">${value}</strong>
        <span>${escapeHtml(item.scale?.right_label || "右侧")}</span>
      </div>
      <button class="ghost-button" id="sliderConfirm" type="button">确认当前选择</button>
    </div>
  `;
}

function renderReflection(item) {
  const value = responses[item.id] || "";
  return `<textarea class="textarea" id="reflectionInput" placeholder="写下真实经历、原因判断、后续改变。开放题目前只保存，不自动诊断。">${escapeHtml(value)}</textarea>`;
}

function renderBehaviorEvidence(item) {
  const selected = new Set(Array.isArray(responses[item.id]) ? responses[item.id] : []);
  return `<div class="checkbox-grid">${Object.entries(item.options || {})
    .map(([key, text]) => {
      const checked = selected.has(key) ? "checked" : "";
      return `<label class="option-card"><input type="checkbox" value="${key}" ${checked} /> <span><strong>${key}.</strong> ${escapeHtml(text)}</span></label>`;
    })
    .join("")}</div>`;
}

function bindAnswerControl(item) {
  if (item.type === "situational_judgment") {
    el.itemStage.querySelectorAll("[data-option]").forEach((button) => {
      button.addEventListener("click", () => {
        responses[item.id] = button.dataset.option;
        saveResponses();
        renderChapters();
        renderItem();
      });
    });
  }

  if (item.type === "ranking") {
    el.itemStage.querySelectorAll("[data-rank-move]").forEach((button) => {
      button.addEventListener("click", () => {
        const optionKeys = Object.keys(item.options || {});
        const order = Array.isArray(responses[item.id]) && responses[item.id].length ? [...responses[item.id]] : optionKeys;
        const index = Number(button.dataset.rankMove);
        const nextIndex = index + Number(button.dataset.direction);
        if (nextIndex < 0 || nextIndex >= order.length) return;
        [order[index], order[nextIndex]] = [order[nextIndex], order[index]];
        responses[item.id] = order;
        saveResponses();
        renderChapters();
        renderItem();
      });
    });
    el.itemStage.querySelector("[data-rank-confirm]")?.addEventListener("click", () => {
      const optionKeys = Object.keys(item.options || {});
      responses[item.id] = Array.isArray(responses[item.id]) && responses[item.id].length ? responses[item.id] : optionKeys;
      saveResponses();
      renderChapters();
      renderItem();
    });
  }

  if (item.type === "slider") {
    const input = el.itemStage.querySelector("#sliderInput");
    const value = el.itemStage.querySelector("#sliderValue");
    input.addEventListener("input", () => {
      value.textContent = input.value;
      responses[item.id] = Number(input.value);
      saveResponses();
      renderChapters();
    });
    el.itemStage.querySelector("#sliderConfirm").addEventListener("click", () => {
      responses[item.id] = Number(input.value);
      saveResponses();
      renderChapters();
      renderItem();
    });
  }

  if (item.type === "reflection") {
    const input = el.itemStage.querySelector("#reflectionInput");
    input.addEventListener("input", () => {
      responses[item.id] = input.value;
      saveResponses();
      renderChapters();
    });
  }

  if (item.type === "behavior_evidence") {
    el.itemStage.querySelectorAll("input[type='checkbox']").forEach((checkbox) => {
      checkbox.addEventListener("change", () => {
        responses[item.id] = Array.from(el.itemStage.querySelectorAll("input[type='checkbox']:checked")).map((entry) => entry.value);
        saveResponses();
        renderChapters();
      });
    });
  }
}

function addWeights(result, weights, multiplier = 1) {
  Object.entries(weights || {}).forEach(([construct, value]) => {
    if (typeof value !== "number") return;
    result.scores[construct] = (result.scores[construct] || 0) + value * multiplier;
    result.evidenceCount[construct] = (result.evidenceCount[construct] || 0) + 1;
  });
}

function scoreItem(item, response, result) {
  const scoring = item.scoring || {};
  if (response === undefined || response === null || response === "") return;

  if (item.type === "situational_judgment") {
    addWeights(result, scoring[String(response)]);
    return;
  }

  if (item.type === "ranking" && Array.isArray(response)) {
    const positionWeights = scoring.position_weights || [];
    const optionWeights = scoring.options || {};
    response.forEach((option, index) => {
      if (index < positionWeights.length) addWeights(result, optionWeights[String(option)], Number(positionWeights[index]));
    });
    return;
  }

  if (item.type === "slider") {
    const numeric = Number(response);
    if (!Number.isFinite(numeric)) return;
    const min = Number(scoring.min || 1);
    const max = Number(scoring.max || 5);
    const midpoint = (min + max) / 2;
    if (numeric < midpoint) addWeights(result, scoring.left, midpoint - numeric);
    if (numeric > midpoint) addWeights(result, scoring.right, numeric - midpoint);
    return;
  }

  if (item.type === "behavior_evidence") {
    const selected = Array.isArray(response) ? response : [response];
    selected.forEach((option) => addWeights(result, scoring.options?.[String(option)]));
    return;
  }

  if (item.type === "reflection") {
    result.unscored.push(item.id);
  }
}

function scoreAll() {
  const result = { scores: {}, evidenceCount: {}, unscored: [] };
  allItems.forEach((item) => {
    if (hasResponse(item)) scoreItem(item, responses[item.id], result);
  });
  return result;
}

function summarize(result) {
  return Object.entries(result.scores)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([construct, rawScore]) => {
      const evidenceCount = result.evidenceCount[construct] || 0;
      const confidence = evidenceCount >= 6 ? "高" : evidenceCount >= 3 ? "中" : "低";
      return { construct, rawScore: Number(rawScore.toFixed(3)), evidenceCount, confidence };
    });
}

function profileForConstruct(construct) {
  const prefix = Object.keys(PROFILE_PREFIXES).find((entry) => construct === entry || construct.startsWith(`${entry}.`));
  return prefix ? PROFILE_PREFIXES[prefix] : "其他信号";
}

function renderReport() {
  const result = scoreAll();
  const summary = summarize(result);
  const grouped = new Map(PROFILE_ORDER.map((profile) => [profile, []]));
  summary.forEach((entry) => grouped.get(profileForConstruct(entry.construct)).push(entry));
  const answered = answeredCount(allItems);
  latestMarkdown = buildMarkdown(summary, result.unscored, answered);

  const profileHtml = PROFILE_ORDER.map((profile) => {
    const entries = grouped.get(profile) || [];
    if (!entries.length) return "";
    return `
      <article class="profile-card">
        <h3>${profile}</h3>
        ${entries.map(renderConstructRow).join("")}
      </article>
    `;
  }).join("");

  el.reportPanel.innerHTML = `
    <div class="report-header">
      <div>
        <p class="eyebrow">Local Report</p>
        <h3>当前报告</h3>
        <p class="report-note">${MODE_LABEL}：已回答 ${answered} / ${allItems.length} 题。分数是规则评分原始值，不是总评、不做淘汰。</p>
      </div>
      <div class="report-actions">
        <button id="copyMarkdownButton" class="ghost-button" type="button">复制 Markdown</button>
        <button id="exportJsonButton" class="ghost-button" type="button">导出答案 JSON</button>
      </div>
    </div>
    <div class="profile-grid">${profileHtml || "<p class='muted'>还没有足够的可评分答案。</p>"}</div>
    ${
      result.unscored.length
        ? `<p class="report-note">开放反思题已保存但未自动评分：${result.unscored.map((id) => `<code>${id}</code>`).join(" ")}</p>`
        : ""
    }
  `;
  el.reportPanel.classList.remove("hidden");
  bindReportActions();
  el.reportPanel.scrollIntoView({ behavior: "smooth", block: "start" });
}

function renderConstructRow(entry) {
  const width = Math.min(100, Math.abs(entry.rawScore) * 12);
  const align = entry.rawScore < 0 ? "margin-left:auto;" : "";
  return `
    <div class="construct-row">
      <div class="construct-top">
        <span><code>${escapeHtml(entry.construct)}</code></span>
        <strong>${entry.rawScore} · 置信度${entry.confidence}</strong>
      </div>
      <div class="score-track"><div class="score-bar" style="width:${width}%;${align}"></div></div>
      <span class="muted">证据题项数：${entry.evidenceCount}</span>
    </div>
  `;
}

function buildMarkdown(summary, unscored, answered) {
  const groups = new Map(PROFILE_ORDER.map((profile) => [profile, []]));
  summary.forEach((entry) => groups.get(profileForConstruct(entry.construct)).push(entry));
  const lines = [
    "# ScholarFit Report",
    "",
    "This report is for self-reflection only. It is not a diagnosis, selection decision, or PhD suitability verdict.",
    "",
    `Mode: ${MODE_LABEL}`,
    "",
    `Answered items: ${answered} / ${allItems.length}`,
    "",
  ];
  PROFILE_ORDER.forEach((profile) => {
    const entries = groups.get(profile) || [];
    if (!entries.length) return;
    lines.push(`## ${profile}`, "");
    entries.forEach((entry) => {
      lines.push(`- \`${entry.construct}\`: raw score ${entry.rawScore}, evidence count ${entry.evidenceCount}, confidence ${entry.confidence}`);
    });
    lines.push("");
  });
  if (unscored.length) {
    lines.push("## Unscored Reflection Items", "");
    unscored.forEach((id) => lines.push(`- \`${id}\` requires human or optional LLM rubric coding.`));
    lines.push("");
  }
  lines.push("## Interpretation Boundary", "", "Scores reflect response patterns in this item bank. They should be interpreted together with context, opportunity, resources, and real-world constraints.");
  return `${lines.join("\n")}\n`;
}

function bindReportActions() {
  document.querySelector("#copyMarkdownButton")?.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(latestMarkdown);
      alert("Markdown 报告已复制。");
    } catch {
      alert("当前浏览器不允许直接复制。你可以从页面报告中手动选择文本。");
    }
  });
  document.querySelector("#exportJsonButton")?.addEventListener("click", () => {
    const blob = new Blob([JSON.stringify({ responses }, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "scholarfit_responses.json";
    link.click();
    URL.revokeObjectURL(url);
  });
}

el.prevButton.addEventListener("click", () => {
  currentIndex -= 1;
  renderItem();
});

el.nextButton.addEventListener("click", () => {
  const items = visibleItems();
  if (currentIndex >= items.length - 1) {
    renderReport();
  } else {
    currentIndex += 1;
    renderItem();
  }
});

el.showReportButton.addEventListener("click", renderReport);

el.clearButton.addEventListener("click", () => {
  if (!confirm("确认清空当前浏览器保存的 ScholarFit 答案？")) return;
  responses = {};
  saveResponses();
  renderChapters();
  renderItem();
  el.reportPanel.classList.add("hidden");
});

el.modeTitle.textContent = MODE_LABEL;
el.modeDescription.textContent = MODE_DESCRIPTION;
el.modeText.textContent = `当前模式：${MODE_LABEL} · ${MODE_DESCRIPTION}`;

renderChapters();
renderProgress();
renderItem();

if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./sw.js").catch(() => {
      // Offline caching is optional; the app still works without it.
    });
  });
}
