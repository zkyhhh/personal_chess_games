﻿const data = [
  {
    name: "GPT-5.3",
    developer: "OpenAI",
    version: "2025-02",
    tags: ["chat", "vision", "audio"],
    features: ["顶级推理", "多模态", "实时对话"],
  },
  {
    name: "GPT-5.2",
    developer: "OpenAI",
    version: "2025-02",
    tags: ["chat", "vision", "audio"],
    features: ["增强推理", "上下文工程", "多模态"],
  },
  {
    name: "GPT-5",
    developer: "OpenAI",
    version: "2025-01",
    tags: ["chat", "vision", "audio"],
    features: ["下一代架构", "语言理解", "生成能力"],
  },
  {
    name: "GPT-5-Codex",
    developer: "OpenAI",
    version: "2025-09",
    tags: ["code", "agent"],
    features: ["AI程序员", "独立开发", "代码生成"],
  },
  {
    name: "GPT-4o",
    developer: "OpenAI",
    version: "2024-08",
    tags: ["chat", "vision", "audio"],
    features: ["实时对话", "图像理解", "语音交互"],
  },
  {
    name: "GPT-4.1",
    developer: "OpenAI",
    version: "2025-04",
    tags: ["chat", "code"],
    features: ["文档分析", "代码生成", "推理"],
  },
  {
    name: "GPT-4o mini",
    developer: "OpenAI",
    version: "2024-07",
    tags: ["chat", "vision"],
    features: ["低成本", "快速响应", "多模态"],
  },
  {
    name: "o1",
    developer: "OpenAI",
    version: "2024-12",
    tags: ["chat", "code"],
    features: ["复杂推理", "数学问题", "科学计算"],
  },
  {
    name: "o3-mini",
    developer: "OpenAI",
    version: "2025-01",
    tags: ["chat", "code"],
    features: ["高效推理", "代码优化", "问题解决"],
  },
  {
    name: "Claude 3.5 Sonnet",
    developer: "Anthropic",
    version: "2024-10",
    tags: ["chat", "code"],
    features: ["长文写作", "安全对齐", "逻辑推理"],
  },
  {
    name: "Claude 3.5 Haiku",
    developer: "Anthropic",
    version: "2024-11",
    tags: ["chat"],
    features: ["极速响应", "轻量级", "日常对话"],
  },
  {
    name: "Claude 3 Opus",
    developer: "Anthropic",
    version: "2024-02",
    tags: ["chat", "code"],
    features: ["深度分析", "创意写作", "复杂任务"],
  },
  {
    name: "Gemini 1.5 Pro",
    developer: "Google",
    version: "2024-02",
    tags: ["chat", "vision", "audio"],
    features: ["多模态", "视频理解", "超长文本"],
  },
  {
    name: "Gemini 1.5 Flash",
    developer: "Google",
    version: "2024-05",
    tags: ["chat", "vision"],
    features: ["高速处理", "实时响应", "轻量级"],
  },
  {
    name: "Gemini 2.0 Flash",
    developer: "Google",
    version: "2024-12",
    tags: ["chat", "vision", "audio"],
    features: ["原生多模态", "实时流式", "高效能"],
  },
  {
    name: "Llama 3.1",
    developer: "Meta",
    version: "2024-07",
    tags: ["chat", "code"],
    features: ["开源", "多语言", "长上下文"],
  },
  {
    name: "Llama 3.2",
    developer: "Meta",
    version: "2024-09",
    tags: ["chat", "vision"],
    features: ["图像理解", "轻量级", "边缘设备"],
  },
  {
    name: "Llama 3.3",
    developer: "Meta",
    version: "2024-12",
    tags: ["chat", "code"],
    features: ["70B参数", "多语言", "开源"],
  },
  {
    name: "Qwen 2.5",
    developer: "Alibaba",
    version: "2024-09",
    tags: ["chat", "code", "vision"],
    features: ["中文优化", "代码能力", "多模态"],
  },
  {
    name: "Qwen-VL",
    developer: "Alibaba",
    version: "2024-01",
    tags: ["vision"],
    features: ["图像理解", "OCR识别", "视觉问答"],
  },
  {
    name: "Kimi k1.5",
    developer: "Moonshot",
    version: "2025-01",
    tags: ["chat"],
    features: ["200万字符", "长文总结", "中文优化"],
  },
  {
    name: "Mistral Large 2",
    developer: "Mistral",
    version: "2024-07",
    tags: ["chat", "code"],
    features: ["多语言", "代码生成", "函数调用"],
  },
  {
    name: "Mixtral 8x22B",
    developer: "Mistral",
    version: "2024-04",
    tags: ["chat", "code"],
    features: ["MoE架构", "高效推理", "开源"],
  },
  {
    name: "Codestral",
    developer: "Mistral",
    version: "2024-05",
    tags: ["code"],
    features: ["代码补全", "80+语言", "开发者工具"],
  },
  {
    name: "DeepSeek-V3",
    developer: "DeepSeek",
    version: "2024-12",
    tags: ["chat", "code"],
    features: ["671B参数", "MoE架构", "中文优化"],
  },
  {
    name: "DeepSeek-R1",
    developer: "DeepSeek",
    version: "2025-01",
    tags: ["chat", "code", "agent"],
    features: ["链式推理", "复杂任务", "工具使用"],
  },
  {
    name: "DeepSeek-Coder-V2",
    developer: "DeepSeek",
    version: "2024-06",
    tags: ["code"],
    features: ["代码生成", "Bug修复", "代码解释"],
  },
  {
    name: "Sora",
    developer: "OpenAI",
    version: "2024-12",
    tags: ["vision"],
    features: ["视频生成", "多镜头", "场景一致性"],
  },
  {
    name: "DALL-E 3",
    developer: "OpenAI",
    version: "2023-10",
    tags: ["vision"],
    features: ["文生图", "高质量", "风格多样"],
  },
  {
    name: "Midjourney v7",
    developer: "Midjourney",
    version: "2025-02",
    tags: ["vision"],
    features: ["艺术风格", "高质量", "创意图像"],
  },
  {
    name: "Stable Diffusion 3.5",
    developer: "Stability AI",
    version: "2024-10",
    tags: ["vision"],
    features: ["文生图", "开源", "本地部署"],
  },
  {
    name: "Flux 1.1 Pro",
    developer: "Black Forest Labs",
    version: "2024-10",
    tags: ["vision"],
    features: ["细节丰富", "文本渲染", "开源"],
  },
  {
    name: "Whisper v3",
    developer: "OpenAI",
    version: "2023-11",
    tags: ["audio"],
    features: ["语音转文字", "多语言", "开源"],
  },
  {
    name: "ElevenLabs v3",
    developer: "ElevenLabs",
    version: "2024-08",
    tags: ["audio"],
    features: ["逼真语音", "多语言", "情感表达"],
  },
  {
    name: "Suno v4",
    developer: "Suno",
    version: "2024-11",
    tags: ["audio"],
    features: ["AI作曲", "歌词生成", "多风格"],
  },
  {
    name: "Udio v1.5",
    developer: "Udio",
    version: "2024-08",
    tags: ["audio"],
    features: ["音乐生成", "人声合成", "风格多样"],
  },
  {
    name: "Runway Gen-3 Alpha",
    developer: "Runway",
    version: "2024-06",
    tags: ["vision"],
    features: ["视频生成", "视频编辑", "特效制作"],
  },
  {
    name: "Pika 2.0",
    developer: "Pika Labs",
    version: "2024-12",
    tags: ["vision"],
    features: ["视频生成", "风格转换", "动画制作"],
  },
  {
    name: "Luma Dream Machine 1.6",
    developer: "Luma AI",
    version: "2024-10",
    tags: ["vision"],
    features: ["视频生成", "3D建模", "场景重建"],
  },
  {
    name: "Stable Video 1.1",
    developer: "Stability AI",
    version: "2024-03",
    tags: ["vision"],
    features: ["图生视频", "视频编辑", "开源"],
  },
  {
    name: "Copilot",
    developer: "Microsoft",
    version: "2024",
    tags: ["chat", "code", "agent"],
    features: ["Office集成", "代码辅助", "搜索增强"],
  },
  {
    name: "GitHub Copilot",
    developer: "GitHub",
    version: "2024",
    tags: ["code"],
    features: ["代码补全", "自然语言编程", "IDE集成"],
  },
  {
    name: "Cursor",
    developer: "Cursor",
    version: "0.45",
    tags: ["code", "agent"],
    features: ["代码生成", "代码重构", "智能编辑"],
  },
  {
    name: "Windsurf",
    developer: "Codeium",
    version: "1.2",
    tags: ["code", "agent"],
    features: ["Cascade工作流", "多文件编辑", "智能代理"],
  },
  {
    name: "Trae",
    developer: "字节跳动",
    version: "1.0",
    tags: ["code", "agent"],
    features: ["Builder模式", "多模态", "免费使用"],
  },
  {
    name: "Perplexity",
    developer: "Perplexity",
    version: "2024",
    tags: ["chat", "agent"],
    features: ["实时搜索", "信息整合", "引用来源"],
  },
  {
    name: "Grok-3",
    developer: "xAI",
    version: "2025-02",
    tags: ["chat", "code", "vision"],
    features: ["推理能力", "实时信息", "多模态"],
  },
  {
    name: "Grok-2",
    developer: "xAI",
    version: "2024-08",
    tags: ["chat", "vision"],
    features: ["X平台集成", "实时信息", "幽默风格"],
  },
  {
    name: "Pi",
    developer: "Inflection",
    version: "2024",
    tags: ["chat"],
    features: ["情感对话", "个人助理", "友好交互"],
  },
  {
    name: "Character.AI",
    developer: "Character.AI",
    version: "2024",
    tags: ["chat"],
    features: ["虚拟角色", "角色扮演", "娱乐对话"],
  },
  {
    name: "HuggingChat",
    developer: "Hugging Face",
    version: "2024",
    tags: ["chat", "code"],
    features: ["开源模型", "模型对比", "社区驱动"],
  },
  {
    name: "Cohere Command R+",
    developer: "Cohere",
    version: "2024-04",
    tags: ["chat", "code"],
    features: ["企业应用", "RAG支持", "多语言"],
  },
  {
    name: "Jamba 1.5",
    developer: "AI21 Labs",
    version: "2024-08",
    tags: ["chat"],
    features: ["Mamba+Transformer", "长上下文", "高效能"],
  },
  {
    name: "Nova Pro",
    developer: "Amazon",
    version: "2024-12",
    tags: ["chat", "vision"],
    features: ["云原生", "多模态", "企业集成"],
  },
  {
    name: "Titan Text G1",
    developer: "Amazon",
    version: "2024",
    tags: ["chat", "vision"],
    features: ["Bedrock集成", "多模态", "可定制"],
  },
  {
    name: "Imagen 3",
    developer: "Google",
    version: "2024-12",
    tags: ["vision"],
    features: ["高质量图像", "文本渲染", "照片级真实"],
  },
  {
    name: "Veo 2",
    developer: "Google",
    version: "2024-12",
    tags: ["vision"],
    features: ["高质量视频", "物理模拟", "镜头控制"],
  },
  {
    name: "AutoGen v0.4",
    developer: "Microsoft",
    version: "2024-10",
    tags: ["agent", "code"],
    features: ["多代理协作", "代码执行", "工作流编排"],
  },
  {
    name: "LangChain",
    developer: "LangChain",
    version: "0.3",
    tags: ["agent", "code"],
    features: ["链式调用", "工具集成", "RAG应用"],
  },
  {
    name: "LlamaIndex",
    developer: "LlamaIndex",
    version: "0.12",
    tags: ["agent", "code"],
    features: ["数据索引", "检索增强", "知识库"],
  },
  {
    name: "CrewAI",
    developer: "CrewAI",
    version: "0.100",
    tags: ["agent"],
    features: ["多代理团队", "任务分配", "自动化工作流"],
  },
  {
    name: "D-ID",
    developer: "D-ID",
    version: "2024",
    tags: ["vision", "audio"],
    features: ["数字人视频", "语音合成", "形象克隆"],
  },
  {
    name: "HeyGen",
    developer: "HeyGen",
    version: "2024",
    tags: ["vision", "audio"],
    features: ["视频翻译", "数字人播报", "多语言"],
  },
  {
    name: "Poe",
    developer: "Quora",
    version: "2024",
    tags: ["chat", "agent"],
    features: ["多模型接入", "自定义机器人", "社区分享"],
  },
  {
    name: "You.com",
    developer: "You",
    version: "2024",
    tags: ["chat", "agent"],
    features: ["隐私搜索", "AI总结", "多模型选择"],
  },
  {
    name: "Kimi Researcher",
    developer: "Moonshot",
    version: "2025-01",
    tags: ["agent"],
    features: ["深度研究", "多源分析", "报告生成"],
  },
  {
    name: "Manus",
    developer: "Monica",
    version: "2025-03",
    tags: ["agent"],
    features: ["任务执行", "多步骤规划", "工具调用"],
  },
  {
    name: "Devin",
    developer: "Cognition",
    version: "2024",
    tags: ["code", "agent"],
    features: ["端到端开发", "自主编程", "项目管理"],
  },
  {
    name: "Replit Agent",
    developer: "Replit",
    version: "2024",
    tags: ["code", "agent"],
    features: ["自动编程", "部署上线", "全栈开发"],
  },
  {
    name: "Bolt.new",
    developer: "StackBlitz",
    version: "2024",
    tags: ["code", "agent"],
    features: ["提示词开发", "自动部署", "全栈应用"],
  },
  {
    name: "v0.dev",
    developer: "Vercel",
    version: "2024",
    tags: ["code", "vision"],
    features: ["React组件", "UI设计", "代码生成"],
  },
  {
    name: "Claude Artifacts",
    developer: "Anthropic",
    version: "2024-06",
    tags: ["code", "vision"],
    features: ["实时预览", "React组件", "代码迭代"],
  },
  {
    name: "ChatGPT Canvas",
    developer: "OpenAI",
    version: "2024-10",
    tags: ["chat", "code"],
    features: ["文档协作", "代码编辑", "项目管理"],
  },
  {
    name: "Gemini Canvas",
    developer: "Google",
    version: "2024-12",
    tags: ["chat", "vision", "code"],
    features: ["多模态协作", "实时编辑", "创意工作流"],
  },
  {
    name: "NotebookLM",
    developer: "Google",
    version: "2024",
    tags: ["chat", "agent"],
    features: ["文档分析", "播客生成", "知识管理"],
  },
  {
    name: "Claude Projects",
    developer: "Anthropic",
    version: "2024-05",
    tags: ["chat", "agent"],
    features: ["知识库", "长期记忆", "项目上下文"],
  },
  {
    name: "OpenAI Operator",
    developer: "OpenAI",
    version: "2025-01",
    tags: ["agent"],
    features: ["网页操作", "任务自动化", "浏览器控制"],
  },
  {
    name: "Anthropic Computer Use",
    developer: "Anthropic",
    version: "2024-10",
    tags: ["agent"],
    features: ["桌面控制", "应用操作", "自动化任务"],
  },
  {
    name: "Gemini Deep Research",
    developer: "Google",
    version: "2025-02",
    tags: ["agent"],
    features: ["多源搜索", "报告生成", "研究分析"],
  },
  {
    name: "Gemini 2.5 Pro",
    developer: "Google",
    version: "2025-03",
    tags: ["chat", "code", "vision"],
    features: ["100万上下文", "推理优化", "代码能力"],
  },
  {
    name: "Claude 4 Sonnet",
    developer: "Anthropic",
    version: "2025-05",
    tags: ["chat", "code", "vision"],
    features: ["混合推理", "扩展思考", "视觉理解"],
  },
  {
    name: "Claude 4 Opus",
    developer: "Anthropic",
    version: "2025-05",
    tags: ["chat", "code", "vision"],
    features: ["复杂推理", "长上下文", "高级编程"],
  },
  {
    name: "GPT-4.5",
    developer: "OpenAI",
    version: "2025-02",
    tags: ["chat", "vision"],
    features: ["情感理解", "创意写作", "对话流畅"],
  },
  {
    name: "o3",
    developer: "OpenAI",
    version: "2025-01",
    tags: ["chat", "code"],
    features: ["顶级推理", "科学研究", "复杂问题"],
  }
];

const cards = document.getElementById("cards");
const searchInput = document.getElementById("searchInput");
const clearBtn = document.getElementById("clearBtn");
const filters = document.querySelectorAll(".filter");

function matchesFilter(item, filter) {
  if (filter === "all") return true;
  return item.tags.includes(filter);
}

function matchesSearch(item, query) {
  if (!query) return true;
  const haystack = [item.name, item.developer, item.version, ...item.features].join(" ").toLowerCase();
  return haystack.includes(query.toLowerCase());
}

function render(filter = "all", query = "") {
  cards.innerHTML = "";
  const filtered = data.filter((item) => matchesFilter(item, filter) && matchesSearch(item, query));

  if (filtered.length === 0) {
    cards.innerHTML = '<div class="card"><h3>没有结果</h3><p class="meta">请尝试其他关键词或筛选。</p></div>';
    return;
  }

  filtered.forEach((item) => {
    const el = document.createElement("div");
    el.className = "card";
    el.innerHTML = `
      <h3>${item.name}</h3>
      <p class="meta">开发者：${item.developer} · 版本：${item.version}</p>
      <div class="badges">
        ${item.tags.map((tag) => `<span class="badge">${tag}</span>`).join("")}
      </div>
      <p>功能：${item.features.join(" / ")}</p>
    `;
    cards.appendChild(el);
  });
}

filters.forEach((btn) => {
  btn.addEventListener("click", () => {
    filters.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    render(btn.dataset.filter, searchInput.value.trim());
  });
});

searchInput.addEventListener("input", () => {
  const active = document.querySelector(".filter.active");
  const filter = active ? active.dataset.filter : "all";
  render(filter, searchInput.value.trim());
});

clearBtn.addEventListener("click", () => {
  searchInput.value = "";
  render("all", "");
  filters.forEach((b) => b.classList.remove("active"));
  filters[0].classList.add("active");
});

render();
