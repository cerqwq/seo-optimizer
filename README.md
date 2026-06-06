# 🔍 SEO Optimizer

AI SEO优化工具，支持关键词分析、内容优化、元数据生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔑 关键词分析
- 📝 内容优化
- 🏷️ 元标签生成
- 📊 Schema标记
- 🏢 竞争对手分析
- 🗺️ Sitemap生成

## 🚀 快速开始

```bash
pip install openai

python optimizer.py
```

## 📖 使用

```python
from seo_optimizer import create_optimizer

optimizer = create_optimizer()

# 关键词分析
keywords = optimizer.analyze_keywords("Python编程", 10)

# 内容优化
result = optimizer.optimize_content(content, ["Python", "编程"])

# 生成元标签
meta = optimizer.generate_meta_tags("标题", content, ["关键词"])

# 生成Schema
schema = optimizer.generate_schema_markup("Article", {"title": "标题"})

# 竞争对手分析
competitor = optimizer.analyze_competitor("https://example.com", "Python")

# 生成Sitemap
sitemap = optimizer.generate_sitemap(pages)
```

## 📁 项目结构

```
seo-optimizer/
├── optimizer.py   # SEO优化器核心
└── README.md
```

## 📄 许可证

MIT License
