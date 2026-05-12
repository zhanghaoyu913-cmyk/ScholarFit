"""Generate the v0.1 draft ScholarFit item bank.

The generated JSON is intentionally explicit and auditable. The items are
drafts for expert review, not validated psychological instruments.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTERS = {
    1: {
        "chapter": "研究之门",
        "story": "Research Gate",
        "slug": "motivation",
        "themes": [
            "motivation.intrinsic",
            "motivation.identified",
            "motivation.external",
            "motivation.introjected",
            "research_behavior.expectation_calibration",
        ],
        "scenarios": [
            "你同时拿到一个高薪行业 offer 和一个博士 offer。博士方向与你长期关心的问题更接近，但路径更不确定。",
            "家人认为博士学历会让你更有社会地位，但你自己还没有形成稳定研究问题。",
            "你读到一篇论文后连续几天都在想它的漏洞和延伸方向，但短期看不到明确产出。",
            "你想申请博士，但主要担心如果不读会显得自己不够优秀。",
        ],
        "question": "你最可能如何决策或行动？",
    },
    2: {
        "chapter": "文献迷宫",
        "story": "Literature Maze",
        "slug": "literature_maze",
        "themes": [
            "research_self_efficacy.literature_integration",
            "research_behavior.learning_strategy",
            "personality.openness",
            "help_seeking.feedback_use",
            "research_maturity.problem_abstraction",
        ],
        "scenarios": [
            "你进入一个新方向，第一周读了 8 篇论文，但概念、方法和评价指标混在一起。",
            "导师让你下周讲一篇理论论文，你发现证明细节看不懂。",
            "你发现两篇高引用论文对同一问题给出相反结论。",
            "你准备写 related work，但文献数量已经超过 60 篇。",
        ],
        "question": "你下一步最可能怎么做？",
    },
    3: {
        "chapter": "实验废墟",
        "story": "Experiment Ruins",
        "slug": "experiment_ruins",
        "themes": [
            "research_self_efficacy.debugging",
            "conscientiousness.systematicity",
            "emotional_stability.failure_recovery",
            "research_maturity.failure_review",
            "academic_integrity.reproducibility",
        ],
        "scenarios": [
            "你复现一篇论文，官方代码能跑，但结果比论文低 20%。你已经检查三天仍然没有找到原因。",
            "你的实验曲线突然变好，但你不确定是方法有效还是数据泄漏。",
            "一个关键实验连续失败三周，deadline 还剩十天。",
            "你换了随机种子后结论不稳定，但最好的 seed 可以支持你的假设。",
        ],
        "question": "你下一步最可能怎么做？",
    },
    4: {
        "chapter": "导师之塔",
        "story": "Advisor Tower",
        "slug": "advisor_tower",
        "themes": [
            "advisor_fit.feedback_need",
            "advisor_fit.structure_need",
            "advisor_fit.autonomy_tolerance",
            "advisor_fit.resource_dependency",
            "advisor_fit.career_alignment",
        ],
        "scenarios": [
            "导师 A 每周开会、任务明确、产出压力大；导师 B 方向更契合你，但一个月才深度讨论一次。",
            "你进组后发现导师经常只给开放问题，很少拆解具体步骤。",
            "组会批评非常直接，有时会当众指出实验设计问题。",
            "你的长期目标偏产业研究，但候选导师更期待学生走纯学术路线。",
        ],
        "question": "你最可能如何选择或沟通？",
    },
    5: {
        "chapter": "同行审判",
        "story": "Peer Review Trial",
        "slug": "peer_review_trial",
        "themes": [
            "academic_integrity.transparency",
            "emotional_stability.criticism_recovery",
            "research_self_efficacy.writing",
            "research_maturity.revision_strategy",
            "agreeableness.feedback_acceptance",
        ],
        "scenarios": [
            "论文被拒，reviewer 质疑你的核心假设并指出实验不足。",
            "reviewer 明显误解了你的方法，但语气很强硬。",
            "合作者建议弱化一个不利实验结果，让故事更顺。",
            "你收到大修意见，需要在两周内补实验和重写 discussion。",
        ],
        "question": "你下一步最可能怎么做？",
    },
    6: {
        "chapter": "方向岔路",
        "story": "Direction Crossroads",
        "slug": "direction_crossroads",
        "themes": [
            "direction_interest.theoretical",
            "direction_interest.experimental",
            "direction_interest.engineering_system",
            "direction_interest.embodied",
            "research_maturity.explore_exploit_balance",
        ],
        "scenarios": [
            "你参与一个机器人项目，系统失败原因可能来自感知、控制、仿真差距或任务规划。",
            "你发现热门方向论文机会多，但真正吸引你的是一个更冷门的机制问题。",
            "你的项目可以继续堆工程，也可以转向解释为什么方法有效。",
            "你有机会加入跨学科项目，但需要学习陌生领域语言和方法。",
        ],
        "question": "你更可能优先推进哪条路径？",
    },
    7: {
        "chapter": "孤独长夜",
        "story": "Lonely Night",
        "slug": "lonely_night",
        "themes": [
            "stress_recovery.restoration",
            "stress_recovery.support_system",
            "stress_recovery.failure_attribution",
            "stress_recovery.burnout_warning",
            "emotional_stability.uncertainty_tolerance",
        ],
        "scenarios": [
            "你连续两个月投入很高但没有可展示进展，开始怀疑自己是否适合科研。",
            "同组同学连续发论文，你的项目还卡在数据和方法问题上。",
            "你一想到组会汇报就失眠，因为结果还不稳定。",
            "你发现自己已经很久没有休息，但停下来又会有强烈负罪感。",
        ],
        "question": "你最可能如何处理当前状态？",
    },
    8: {
        "chapter": "创造之火",
        "story": "Creative Fire",
        "slug": "creative_fire",
        "themes": [
            "research_maturity.problem_finding",
            "personality.openness",
            "research_maturity.mechanism_reasoning",
            "research_maturity.long_term_thread",
            "growth.next_90_days",
        ],
        "scenarios": [
            "你读完一个方向的 30 篇论文后，感觉大家都在优化指标，但问题定义本身可能有缺陷。",
            "你有一个反主流想法，但导师担心它风险太高、短期不容易发。",
            "你发现两个领域的方法可以连接，但还没有明确证明或实验设计。",
            "你已经做出一个可发表的小改进，但它和你真正想追的问题关系不大。",
        ],
        "question": "你下一步最可能怎么做？",
    },
}

SJT_OPTIONS = {
    "A": "先暂停判断，列出可验证假设、约束条件和下一步证据。",
    "B": "优先寻找已有模板或他人建议，尽快获得外部反馈。",
    "C": "选择短期最容易产生结果的路径，先保证可见产出。",
    "D": "回到原始问题，重新定义目标、假设和评价标准。",
    "E": "继续凭直觉推进，等出现更大问题时再系统复盘。",
}

RANKING_OPTIONS = {
    "A": "系统拆解问题并记录证据。",
    "B": "主动找导师、同学或领域内的人做一次反馈讨论。",
    "C": "先恢复状态，再安排下一轮行动。",
    "D": "切换到短期更稳妥或更容易展示的任务。",
    "E": "回到文献、数据或原始需求，检查假设是否成立。",
}

BEHAVIOR_OPTIONS = {
    "A": "精读并整理过 10 篇以上论文。",
    "B": "复现过论文、开源项目或公开实验。",
    "C": "写过技术报告、survey、研究计划或论文草稿。",
    "D": "主动找老师、博士生或同行讨论过研究问题。",
    "E": "做过持续超过 1 个月的项目。",
    "F": "做过实验失败、项目失败或学习失败复盘。",
    "G": "维护过 GitHub 仓库、实验记录或可复现材料。",
}


def make_chapter(chapter_id: int, cfg: dict) -> dict:
    chapter = cfg["chapter"]
    themes = cfg["themes"]
    items = []

    for idx, scenario in enumerate(cfg["scenarios"], start=1):
        items.append(
            {
                "id": f"CH{chapter_id}_SJT_{idx:03d}",
                "chapter": chapter,
                "type": "situational_judgment",
                "constructs": themes[:4],
                "scenario": scenario,
                "question": cfg["question"],
                "options": SJT_OPTIONS,
                "scoring": {
                    "A": {themes[0]: 1, themes[1]: 1, "research_maturity.evidence_reasoning": 1},
                    "B": {"help_seeking.feedback_use": 1, themes[1]: 0.5, "advisor_fit.feedback_need": 0.5},
                    "C": {"research_behavior.short_term_output_orientation": 1, themes[0]: -0.5},
                    "D": {themes[0]: 1, "research_maturity.problem_abstraction": 1, themes[-1]: 0.5},
                    "E": {"research_behavior.random_walk_risk": 1, themes[1]: -1},
                },
                "reporting_rule": "解释科研行为倾向、适配环境与成长建议，不输出适合/不适合读博。",
                "validation_status": "draft",
            }
        )

    for idx in range(1, 3):
        items.append(
            {
                "id": f"CH{chapter_id}_RANK_{idx:03d}",
                "chapter": chapter,
                "type": "ranking",
                "constructs": [
                    themes[0],
                    themes[1],
                    "help_seeking.feedback_use",
                    "stress_recovery.restoration",
                    "research_behavior.short_term_output_orientation",
                ],
                "scenario": f"在“{chapter}”阶段，你面临多个互相竞争的行动选择。",
                "question": "请按你最可能采取的顺序排序。",
                "options": RANKING_OPTIONS,
                "scoring": {
                    "position_weights": [2, 1, 0, -1, -2],
                    "options": {
                        "A": {themes[1]: 1, "research_maturity.evidence_reasoning": 1},
                        "B": {"help_seeking.feedback_use": 1, "advisor_fit.feedback_need": 0.5},
                        "C": {"stress_recovery.restoration": 1, "emotional_stability.failure_recovery": 0.5},
                        "D": {"research_behavior.short_term_output_orientation": 1},
                        "E": {themes[0]: 1, "research_maturity.problem_abstraction": 0.5},
                    },
                },
                "reporting_rule": "排序题用于估计优先级，不把任一选择解释为人格缺陷。",
                "validation_status": "draft",
            }
        )

    slider_pairs = [
        (
            "先建立理论框架",
            "先做实验原型",
            {"direction_interest.theoretical": 1},
            {"direction_interest.experimental": 1, "direction_interest.engineering_system": 0.5},
        ),
        (
            "需要明确任务和反馈",
            "可以在模糊问题中自驱探索",
            {"advisor_fit.structure_need": 1, "advisor_fit.feedback_need": 0.5},
            {"advisor_fit.autonomy_tolerance": 1, "research_maturity.problem_finding": 0.5},
        ),
    ]
    for idx, (left_label, right_label, left_score, right_score) in enumerate(slider_pairs, start=1):
        items.append(
            {
                "id": f"CH{chapter_id}_SLIDER_{idx:03d}",
                "chapter": chapter,
                "type": "slider",
                "constructs": list(left_score.keys()) + list(right_score.keys()),
                "scenario": f"在“{chapter}”阶段，你需要选择一种推进方式。",
                "question": "你更接近哪一侧？",
                "scale": {"min": 1, "max": 5, "left_label": left_label, "right_label": right_label},
                "scoring": {"min": 1, "max": 5, "left": left_score, "right": right_score},
                "reporting_rule": "滑条解释为连续偏好，不作为优劣判断。",
                "validation_status": "draft",
            }
        )

    items.append(
        {
            "id": f"CH{chapter_id}_REFLECT_001",
            "chapter": chapter,
            "type": "reflection",
            "constructs": [
                "research_maturity.metacognition",
                "stress_recovery.failure_attribution",
                "growth.next_90_days",
            ],
            "scenario": f"请回忆一次与你的“{chapter}”主题相近的真实经历。",
            "question": "当时发生了什么？你如何判断原因？后来做了什么改变？",
            "scoring": {
                "rubric": {
                    "attribution": "可控因素 vs 全局自我否定",
                    "specificity": "是否具体定位原因",
                    "strategy_change": "是否产生后续策略",
                    "emotional_regulation": "是否能恢复并继续推进",
                    "research_maturity": "是否抽象出可迁移经验",
                }
            },
            "reporting_rule": "开放题需人工或可选 LLM 按 rubric 编码，不直接诊断。",
            "validation_status": "draft",
        }
    )

    items.append(
        {
            "id": f"CH{chapter_id}_BEHAVIOR_001",
            "chapter": chapter,
            "type": "behavior_evidence",
            "constructs": [
                "research_behavior.prior_experience",
                "research_self_efficacy.literature_integration",
                "research_self_efficacy.debugging",
                "academic_integrity.reproducibility",
            ],
            "scenario": "过去 6 个月，你做过哪些与科研准备相关的事情？",
            "question": "请选择所有符合的行为证据。",
            "options": BEHAVIOR_OPTIONS,
            "scoring": {
                "options": {
                    "A": {
                        "research_self_efficacy.literature_integration": 1,
                        "research_behavior.prior_experience": 0.5,
                    },
                    "B": {
                        "research_self_efficacy.debugging": 1,
                        "research_behavior.prior_experience": 0.5,
                    },
                    "C": {
                        "research_self_efficacy.writing": 1,
                        "research_behavior.prior_experience": 0.5,
                    },
                    "D": {"help_seeking.feedback_use": 1, "research_behavior.prior_experience": 0.5},
                    "E": {
                        "conscientiousness.long_term_follow_through": 1,
                        "research_behavior.prior_experience": 0.5,
                    },
                    "F": {
                        "research_maturity.failure_review": 1,
                        "stress_recovery.failure_attribution": 0.5,
                    },
                    "G": {
                        "academic_integrity.reproducibility": 1,
                        "conscientiousness.systematicity": 0.5,
                    },
                }
            },
            "reporting_rule": "行为证据用于校准自评，但要考虑机会、资源与背景差异。",
            "validation_status": "draft",
        }
    )

    return {
        "chapter_id": chapter_id,
        "chapter": chapter,
        "story_name": cfg["story"],
        "version": "0.1.0-draft",
        "language": "zh-CN",
        "items": items,
    }


def main() -> None:
    item_bank_dir = ROOT / "item_bank"
    item_bank_dir.mkdir(exist_ok=True)
    all_items = []
    for chapter_id, cfg in CHAPTERS.items():
        payload = make_chapter(chapter_id, cfg)
        all_items.extend(payload["items"])
        path = item_bank_dir / f"chapter_{chapter_id}_{cfg['slug']}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme = (
        "# Item Bank\n\n"
        "This directory contains the v0.1 draft story-based item bank.\n\n"
        "Each chapter contains 10 items:\n\n"
        "- 4 situational judgment items\n"
        "- 2 ranking items\n"
        "- 2 slider items\n"
        "- 1 reflection item\n"
        "- 1 behavior evidence item\n\n"
        f"Total v0.1 draft size: {len(all_items)} items.\n\n"
        "All items are draft content. They require expert review, cognitive interviews, pilot testing, reliability analysis, validity evidence, and fairness checks before any strong interpretation.\n"
    )
    (item_bank_dir / "README.md").write_text(readme, encoding="utf-8")

    sample_item = next(item for item in all_items if item["id"] == "CH3_SJT_001")
    (ROOT / "examples" / "sample_item_bank.json").write_text(
        json.dumps({"chapter": "实验废墟", "items": [sample_item]}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    sample_responses = {
        "responses": {
            "CH3_SJT_001": "A",
            "CH3_SJT_002": "D",
            "CH3_RANK_001": ["A", "E", "B", "C", "D"],
            "CH3_SLIDER_001": 4,
            "CH3_BEHAVIOR_001": ["A", "B", "F", "G"],
            "CH3_REFLECT_001": "我曾经复现实验失败，后来发现数据预处理和评价脚本不一致。我把配置记录下来，并请同学复核了一次。",
        }
    }
    (ROOT / "examples" / "sample_responses.json").write_text(
        json.dumps(sample_responses, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
