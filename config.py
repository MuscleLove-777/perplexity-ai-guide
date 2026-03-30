"""Perplexity AI検索革命ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Perplexity AI検索革命ガイド"
BLOG_DESCRIPTION = "Perplexity AIの使い方・最新機能・料金プラン・活用術を毎日更新。AI検索エンジンPerplexityを使いこなすための日本語完全ガイド。"
BLOG_URL = "https://musclelove-777.github.io/perplexity-ai-guide"
BLOG_TAGLINE = "AI検索の未来を切り開くPerplexity完全ガイド"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/perplexity-ai-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Perplexity 使い方",
    "Perplexity 料金・プラン",
    "Perplexity Pro",
    "Perplexity vs Google",
    "Perplexity API",
    "Perplexity 最新ニュース",
    "AI検索エンジン比較",
    "Perplexity 活用事例",
]

THEME = {
    "primary": "#20b2aa",
    "accent": "#1a8a82",
    "gradient_start": "#20b2aa",
    "gradient_end": "#177d76",
    "dark_bg": "#0a1628",
    "dark_surface": "#142240",
    "light_bg": "#f0fffe",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [8, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Perplexity Pro": [
        {"service": "Perplexity Pro", "url": "https://perplexity.ai/pro", "description": "Perplexity Proに登録する"},
    ],
    "Perplexity": [
        {"service": "Perplexity", "url": "https://perplexity.ai", "description": "Perplexity公式サイト"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8088

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
