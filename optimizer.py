"""
SEO Optimizer - AI SEO优化工具
支持关键词分析、内容优化、元数据生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class SEOOptimizer:
    """
    AI SEO优化工具
    支持：关键词分析、内容优化、元数据生成
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def analyze_keywords(self, topic: str, count: int = 10) -> List[Dict]:
        """分析关键词"""
        if not self.client:
            return [{"error": "LLM客户端未配置"}]

        prompt = f"""请为"{topic}"生成{count}个SEO关键词：

请返回JSON格式：
[
    {{"keyword": "关键词", "search_volume": "high/medium/low", "competition": "high/medium/low", "relevance": 1-10}}
]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [{"keyword": content}]

    def optimize_content(self, content: str, keywords: List[str] = None) -> Dict:
        """优化内容"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        keywords_text = ", ".join(keywords) if keywords else ""

        prompt = f"""请优化以下内容的SEO：

内容：
{content}

目标关键词：{keywords_text}

请返回JSON格式：
{{
    "optimized_content": "优化后的内容",
    "title": "SEO标题",
    "meta_description": "元描述",
    "suggestions": ["建议1", "建议2"],
    "keyword_density": "关键词密度"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimized": content}

    def generate_meta_tags(self, title: str, content: str, keywords: List[str] = None) -> Dict:
        """生成元标签"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为以下页面生成SEO元标签：

标题：{title}
内容摘要：{content[:200]}
关键词：{', '.join(keywords or [])}

请返回JSON格式：
{{
    "title_tag": "标题标签",
    "meta_description": "元描述",
    "og_title": "Open Graph标题",
    "og_description": "Open Graph描述",
    "keywords": ["关键词1", "关键词2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"meta": content}

    def generate_schema_markup(self, page_type: str, data: Dict) -> str:
        """生成Schema标记"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{page_type}类型的Schema.org JSON-LD标记：

数据：{json.dumps(data, ensure_ascii=False)}

请返回完整的JSON-LD代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def analyze_competitor(self, url: str, topic: str) -> Dict:
        """分析竞争对手"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析{url}在"{topic}"方面的SEO策略：

请返回JSON格式：
{{
    "strengths": ["优势1", "优势2"],
    "weaknesses": ["劣势1", "劣势2"],
    "keywords": ["使用的关键词"],
    "content_strategy": "内容策略分析",
    "recommendations": ["建议1", "建议2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def generate_sitemap(self, pages: List[Dict]) -> str:
        """生成Sitemap"""
        if not self.client:
            return "LLM客户端未配置"

        pages_text = json.dumps(pages, ensure_ascii=False)

        prompt = f"""请根据以下页面信息生成XML Sitemap：

{pages_text}

请返回完整的XML格式Sitemap："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_optimizer(**kwargs) -> SEOOptimizer:
    """创建SEO优化器"""
    return SEOOptimizer(**kwargs)


if __name__ == "__main__":
    optimizer = create_optimizer()

    print("SEO Optimizer")
    print()

    # 测试
    keywords = optimizer.analyze_keywords("Python编程", 5)
    print("Keywords:")
    for kw in keywords[:3]:
        print(f"  - {kw}")
