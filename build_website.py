#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindCraft Zen Multi-Language Website & Privacy Policy Generator
Generates index.html and privacy.html supporting all 10 languages:
zh-Hant (繁體中文), zh-Hans (简体中文), en (English), ja (日本語), ko (한국어),
de (Deutsch), fr (Français), es (Español), vi (Tiếng Việt), th (ไทย)
"""

import json
import os

LANGUAGES = [
    {"code": "zh-Hant", "name": "繁體中文"},
    {"code": "zh-Hans", "name": "简体中文"},
    {"code": "en", "name": "English"},
    {"code": "ja", "name": "日本語"},
    {"code": "ko", "name": "한국어"},
    {"code": "de", "name": "Deutsch"},
    {"code": "fr", "name": "Français"},
    {"code": "es", "name": "Español"},
    {"code": "vi", "name": "Tiếng Việt"},
    {"code": "th", "name": "ไทย"},
]

INDEX_DATA = {
    "zh-Hant": {
        "nav_title": "心象天工",
        "nav_subtitle": "MindCraft Zen",
        "nav_crafts": "四大古智",
        "nav_tech": "端側禪境",
        "nav_tiers": "匠人典藏",
        "nav_privacy": "隱私政策",
        "nav_terms": "使用條款 (EULA)",
        "nav_support": "✉️ 客服支援",
        "footer_support_label": "官方支援與客服信箱",
        "hero_badge": "五千年東方古智 · Apple 端側神經網路專注工坊",
        "hero_title": "心象天工 · 木構與禪",
        "hero_subtitle": "沈浸於 3D 魯班鎖、2D 宋代燕幾圖、九連環與洛書華容道。在榫卯咬合的清脆回響中，尋回內心的寧靜與專注。",
        "hero_cta": "前往 App Store 下載",
        "hero_cta_sub": "支援 iPhone、iPad 與 Apple Vision Pro",
        "crafts_heading": "五千年東方智慧 · 四大榫卯與格雷機關",
        "crafts_sub": "不著一釘一鉚，純憑空間拓撲、二進位遞歸與奇正相生。",
        "craft_1_title": "3D 魯班鎖 (孔明鎖)",
        "craft_1_desc": "六子聯方、八角乾坤。三維空間 360 度自由旋轉拆解，感受千斤承重不費一釘一鉚的東方空間拓撲哲學。",
        "craft_2_title": "2D 宋代燕幾圖",
        "craft_2_desc": "南宋黃伯思宴幾之譜，七巧之祖。以案几之離合變幻，演繹宋代文人雅士高雅審美與多維空間組合幾何。",
        "craft_3_title": "天道九連環",
        "craft_3_desc": "玉環與雙股金釵交錯。蘊含嚴密二進位格雷碼遞歸天律，一環引一環，解之無窮，修心凝神。",
        "craft_4_title": "洛書華容道",
        "craft_4_desc": "太極生兩儀，九宮布奇正。曹瞞兵敗華容，方寸棋盤間運籌帷幄，體驗東方古兵法之戰略智慧。",
        "tech_heading": "極致純淨 · Apple 前沿科技與禪境心流",
        "tech_sub": "為深層心流而生，拒絕浮躁，回歸純粹專注。",
        "tech_1_title": "100% 端側神經網路",
        "tech_1_desc": "所有 AI 殘局生成與視覺渲染完全於本機晶片執行。零聯網依賴，零伺服器上傳，極致守護個人隱私。",
        "tech_2_title": "TrueDepth 視線專注追蹤",
        "tech_2_desc": "透過前置原深感測相機即時感知凝神狀態，動態微調環境光影與木香白噪音，助您深度沉浸。",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "讀取心率變異度 (HRV)，解題前後即時呈現自律神經放鬆程度與心流專注指數。",
        "tech_4_title": "432Hz 東方五音冥想聲景",
        "tech_4_desc": "收錄千年古琴、空靈編鐘、深山晨雨與擬真木作觸感回饋，帶來視覺、聽覺與觸覺的三重共振。",
        "tiers_heading": "匠人典藏會員方案",
        "tiers_sub": "100% 透過 Apple StoreKit 2 訂閱管理，安全透明，隨時於 Apple ID 取消。",
        "tier_1_title": "月度修行方案",
        "tier_1_badge": "靈活按月訂閱 · 隨時管理",
        "tier_1_feature_1": "解鎖全部 3D 魯班鎖與 2D 燕幾圖高階關卡",
        "tier_1_feature_2": "每日晨曦定志與夜闌解憂東方音療",
        "tier_1_feature_3": "基礎觸控流暢度專注力分析報告",
        "tier_2_title": "年度心流方案 (主要推薦)",
        "tier_2_badge": "含免費體驗期 · 依 App Store 優惠同步",
        "tier_2_feature_1": "完整體驗五千年文明長卷與宗師級機關",
        "tier_2_feature_2": "解鎖端側 AI 無窮榫卯與殘局生成工坊",
        "tier_2_feature_3": "進階 TrueDepth 視線穩定追蹤 & Apple Watch HRV 心流報告",
        "tier_2_feature_4": "無限次夜空放天燈祈福與 10 語雅集猜燈謎",
        "tier_3_title": "終身藏家方案",
        "tier_3_badge": "贈【和田青玉藏家印信】· 永久解鎖",
        "tier_3_feature_1": "一次付清，永久擁有全部五千年歷史章節與未來更新",
        "tier_3_feature_2": "獨家獲贈【終身藏家和田青玉印章】落款特權",
        "tier_3_feature_3": "包含未來 Apple Vision Pro (visionOS) 空間巨型機關擴充包",
        "tier_3_feature_4": "零訂閱壓力，收藏一座靜謐的數字東方工藝博物館",
        "eula_disclosure_title": "Apple App Store 訂閱條款與自動續期說明",
        "eula_disclosure_text": "付款將在確認購買時自您的 Apple ID 帳戶扣款。訂閱會自動續期，除非在當前計費週期結束前至少 24 小時取消。帳戶將在當前週期結束前 24 小時內收取續期費用。購買後您可隨時至 Apple ID 帳戶設定中管理或取消訂閱。免費試用期內取消將不產生任何費用。",
        "footer_rights": "版權所有 © 2026 心象天工 MindCraft Zen 團隊。保留所有權利。",
        "footer_privacy": "隱私權政策",
        "footer_eula": "Apple 標準許可協議 (Standard EULA)",
        "footer_support": "支援與聯絡：howly7777777@gmail.com",
    },
    "zh-Hans": {
        "nav_title": "心象天工",
        "nav_subtitle": "MindCraft Zen",
        "nav_crafts": "四大古智",
        "nav_tech": "端侧禅境",
        "nav_tiers": "匠人典藏",
        "nav_privacy": "隐私政策",
        "nav_terms": "使用条款 (EULA)",
        "nav_support": "✉️ 客服支援",
        "footer_support_label": "官方支援与客服邮箱",
        "hero_badge": "五千年东方古智 · Apple 端侧神经网络专注工坊",
        "hero_title": "心象天工 · 木构与禅",
        "hero_subtitle": "沉浸于 3D 鲁班锁、2D 宋代燕几图、九连环与洛书华容道。在榫卯咬合的清脆回响中，寻回内心的宁静与专注。",
        "hero_cta": "前往 App Store 下载",
        "hero_cta_sub": "支持 iPhone、iPad 与 Apple Vision Pro",
        "crafts_heading": "五千年东方智慧 · 四大榫卯与格雷机关",
        "crafts_sub": "不着一钉一铆，纯凭空间拓扑、二进制递归与奇正相生。",
        "craft_1_title": "3D 鲁班锁 (孔明锁)",
        "craft_1_desc": "六子联方、八角乾坤。三维空间 360 度自由旋转拆解，感受千斤承重不费一钉一铆的东方空间拓扑哲学。",
        "craft_2_title": "2D 宋代燕几图",
        "craft_2_desc": "南宋黄伯思宴几之谱，七巧之祖。以案几之离合变幻，演译宋代文人雅士高雅审美与多维空间组合几何。",
        "craft_3_title": "天道九连环",
        "craft_3_desc": "玉环与双股金钗交错。蕴含严密二进制格雷码递归天律，一环引一环，解之无穷，修心凝神。",
        "craft_4_title": "洛书华容道",
        "craft_4_desc": "太极生两仪，九宫布奇正。曹瞒兵败华容，方寸棋盘间运筹帷幄，体验东方古兵法之战略智慧。",
        "tech_heading": "极致纯净 · Apple 前沿科技与禅境心流",
        "tech_sub": "为深层心流而生，拒绝浮躁，回归纯粹专注。",
        "tech_1_title": "100% 端侧神经网络",
        "tech_1_desc": "所有 AI 残局生成与视觉渲染完全于本机芯片执行。零联网依赖，零服务器上传，极致守护个人隐私。",
        "tech_2_title": "TrueDepth 视线专注追踪",
        "tech_2_desc": "透过前置原深感测相机即时感知凝神状态，动态微调环境光影与木香白噪音，助您深度沉浸。",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "读取心率变异度 (HRV)，解题前后即时呈现自律神经放松程度与心流专注指数。",
        "tech_4_title": "432Hz 东方五音冥想声景",
        "tech_4_desc": "收录千年古琴、空灵编钟、深山晨雨与拟真木作触感反馈，带来视觉、听觉与触觉的三重共振。",
        "tiers_heading": "匠人典藏会员方案",
        "tiers_sub": "100% 透过 Apple StoreKit 2 订阅管理，安全透明，随时于 Apple ID 取消。",
        "tier_1_title": "月度修行方案",
        "tier_1_badge": "灵活按月订阅 · 随时管理",
        "tier_1_feature_1": "解锁全部 3D 鲁班锁与 2D 燕几图高阶关卡",
        "tier_1_feature_2": "每日晨曦定志与夜阑解忧东方音疗",
        "tier_1_feature_3": "基础触控流畅度专注力分析报告",
        "tier_2_title": "年度心流方案 (主要推荐)",
        "tier_2_badge": "含免费体验期 · 依 App Store 优惠同步",
        "tier_2_feature_1": "完整体验五千年文明长卷与宗师级机关",
        "tier_2_feature_2": "解锁端侧 AI 无穷榫卯与残局生成工坊",
        "tier_2_feature_3": "进阶 TrueDepth 视线稳定追踪 & Apple Watch HRV 心流报告",
        "tier_2_feature_4": "无限次夜空放天灯祈福与 10 语雅集猜灯谜",
        "tier_3_title": "终身藏家方案",
        "tier_3_badge": "赠【和田青玉藏家印信】· 永久解锁",
        "tier_3_feature_1": "一次付清，永久拥有全部五千年历史章节与未来更新",
        "tier_3_feature_2": "独家获赠【终身藏家和田青玉印章】落款特权",
        "tier_3_feature_3": "包含未来 Apple Vision Pro (visionOS) 空间巨型机关扩充包",
        "tier_3_feature_4": "零订阅压力，收藏一座静谧的数字东方工艺博物馆",
        "eula_disclosure_title": "Apple App Store 订阅条款与自动续期说明",
        "eula_disclosure_text": "付款将在确认购买时自您的 Apple ID 帐户扣款。订阅会自动续期，除非在当前计费周期结束前至少 24 小时取消。帐户将在当前周期结束前 24 小时内收取续期费用。购买后您可随时至 Apple ID 帐户设定中管理或取消订阅。免费试用期内取消将不产生任何费用。",
        "footer_rights": "版权所有 © 2026 心象天工 MindCraft Zen 团队。保留所有权利。",
        "footer_privacy": "隐私权政策",
        "footer_eula": "Apple 标准许可协议 (Standard EULA)",
        "footer_support": "支援与联络：howly7777777@gmail.com",
    },
    "en": {
        "nav_title": "MindCraft Zen",
        "nav_subtitle": "Joinery & Mind",
        "nav_crafts": "4 Ancient Crafts",
        "nav_tech": "Zen Technology",
        "nav_tiers": "Membership",
        "nav_privacy": "Privacy Policy",
        "nav_terms": "Terms of Use (EULA)",
        "nav_support": "✉️ Support",
        "footer_support_label": "Official Support & Inquiries",
        "hero_badge": "5,000 Years of Oriental Joinery · On-Device AI Focus Studio",
        "hero_title": "MindCraft Zen · Joinery & Mind",
        "hero_subtitle": "Immerse yourself in 3D Luban Locks, 2D Song Dynasty Yanji Tables, Nine Linked Rings, and Luoshu Klotski. Rediscover profound inner peace and clarity.",
        "hero_cta": "Download on the App Store",
        "hero_cta_sub": "Crafted for iPhone, iPad & Apple Vision Pro",
        "crafts_heading": "5,000 Years of Heritage · 4 Interlocking Master Crafts",
        "crafts_sub": "Zero nails, zero glue. Pure spatial topology, binary recursion, and timeless oriental balance.",
        "craft_1_title": "3D Luban Interlocking Lock",
        "craft_1_desc": "Six-piece cross and octagonal celestial geometries. Rotate freely in 3D space to unfasten centuries-old mortise-and-tenon architectural wisdom.",
        "craft_2_title": "2D Yanji Tables (Tangram Ancestor)",
        "craft_2_desc": "Huang Bosi's Southern Song dynasty banquet arrangement scroll. Recompose geometric wooden tables to explore refined spatial poetry.",
        "craft_3_title": "Celestial Nine Linked Rings",
        "craft_3_desc": "Hetian jade rings interlocking with golden hairpin loops. Embodying binary Gray code recursion, each move leads to boundless tranquility.",
        "craft_4_title": "Luoshu Klotski Puzzle",
        "craft_4_desc": "Nine-palace cosmic numerology meets historic battlefield strategy. Maneuver through tight passages to achieve tactical breakthrough.",
        "tech_heading": "Pure Zen Sanctuary · Cutting-Edge Apple Intelligence",
        "tech_sub": "Engineered for deep flow and mindfulness. Zero distractions, zero data collection.",
        "tech_1_title": "100% On-Device Neural Engine",
        "tech_1_desc": "All puzzle synthesis, AI assistance, and tactile physics run locally on your device. Zero internet required, zero cloud uploads.",
        "tech_2_title": "TrueDepth Gaze Focus Guidance",
        "tech_2_desc": "Utilizes the front TrueDepth camera to gently gauge mindful gaze stability, adjusting ambient temple lighting to deepen your immersion.",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "Syncs Heart Rate Variability (HRV) locally to visualize your autonomic nervous system calming effect before and after each session.",
        "tech_4_title": "432Hz Oriental Soundscapes",
        "tech_4_desc": "Master Guqin chords, singing bowl resonances, gentle mountain rain, and authentic haptic joinery clicks for complete sensory harmony.",
        "tiers_heading": "Artisan Membership Tiers",
        "tiers_sub": "Powered by Apple StoreKit 2. Fully transparent, manage or cancel anytime via Apple ID Settings.",
        "tier_1_title": "Monthly Practice Plan",
        "tier_1_badge": "Flexible Monthly · Cancel Anytime",
        "tier_1_feature_1": "Unlock all 3D Luban Locks & 2D Yanji Table master stages",
        "tier_1_feature_2": "Daily morning focus & nocturnal soothing soundscapes",
        "tier_1_feature_3": "Touch fluidity & focus flow mindfulness analytics",
        "tier_2_title": "Annual Flow Plan (Recommended)",
        "tier_2_badge": "Free Trial Included · Follows App Store Offer",
        "tier_2_feature_1": "Full access to the 5,000-year historical scroll & grandmaster puzzles",
        "tier_2_feature_2": "Unlock on-device AI infinite joinery & endgame puzzle generation",
        "tier_2_feature_3": "Advanced TrueDepth gaze stability & Apple Watch HRV flow reports",
        "tier_2_feature_4": "Unlimited night sky sky-lantern blessings & 10-language lantern riddles",
        "tier_3_title": "Lifetime Collector Pass",
        "tier_3_badge": "Collector Nephrite Jade Seal · Lifetime Unlock",
        "tier_3_feature_1": "One-time payment for perpetual access to all chapters & future updates",
        "tier_3_feature_2": "Exclusive Hetian Nephrite Jade seal signature privilege",
        "tier_3_feature_3": "Includes upcoming Apple Vision Pro spatial joinery expansion",
        "tier_3_feature_4": "Zero subscription pressure. Collect a serene digital craft museum",
        "eula_disclosure_title": "App Store Auto-Renewing Subscription Terms",
        "eula_disclosure_text": "Payment will be charged to your Apple ID account at confirmation of purchase. Subscription automatically renews unless canceled at least 24 hours before the end of the current period. Your account will be charged for renewal within 24 hours prior to the end of the current period. You can manage and cancel your subscriptions in your App Store account settings after purchase. Any unused portion of a free trial will be forfeited if you cancel.",
        "footer_rights": "Copyright © 2026 MindCraft Zen Team. All rights reserved.",
        "footer_privacy": "Privacy Policy",
        "footer_eula": "Apple Standard EULA",
        "footer_support": "Support & Inquiries: howly7777777@gmail.com",
    },
    "ja": {
        "nav_title": "心象天工",
        "nav_subtitle": "木組みと禅",
        "nav_crafts": "四代伝統工芸",
        "nav_tech": "端側禅体験",
        "nav_tiers": "匠の収蔵",
        "nav_privacy": "プライバシーポリシー",
        "nav_terms": "利用規約 (EULA)",
        "nav_support": "✉️ サポート",
        "footer_support_label": "公式サポート＆お問い合わせ窓口",
        "hero_badge": "中国五千年の伝統木組み · オンデバイスAI集中力スタジオ",
        "hero_title": "心象天工 · 木組みと禅",
        "hero_subtitle": "3D魯班ロック、2D燕幾図、九連環、洛書華容道に没入。精緻な仕口が重なり合う澄んだ響きとともに、心に静寂と集中を取り戻します。",
        "hero_cta": "App Store でダウンロード",
        "hero_cta_sub": "iPhone、iPad、Apple Vision Pro 対応",
        "crafts_heading": "五千年の伝統叡智 · 四大木組み＆トポロジー機構",
        "crafts_sub": "釘も接着剤も一切不使用。純粋な空間幾何学と二進法グレイコードの神秘。",
        "craft_1_title": "3D 魯班ロック (孔明鎖)",
        "craft_1_desc": "六子聯方、八角乾坤。3次元空間で360度自由に回転・分解し、釘を使わずに千斤を支える東洋の空間哲学を体感。",
        "craft_2_title": "2D 宋代 燕幾図 (タングラムの祖)",
        "craft_2_desc": "南宋の学者・黄伯思が考案した宴席家具の幾何学。机の離合変幻を通じて、文人たちの優雅な空間美学を堪能。",
        "craft_3_title": "天道 九連環",
        "craft_3_desc": "玉環と双股金釵の交錯。厳密な二進法グレイコードの天律を宿し、一環を外すごとに心の静寂を深めます。",
        "craft_4_title": "洛書 華容道",
        "craft_4_desc": "太極より陰陽を生じ、九宮に奇正を配す。方寸の盤上で智謀を巡らせ、東洋古代兵法の戦略的奥義を解き明かします。",
        "tech_heading": "純粋な禅の境地 · 最先端 Apple テクノロジー",
        "tech_sub": "深きマインドフルネスのために設計。完全プライベート、広告・データ収集ゼロ。",
        "tech_1_title": "100% オンデバイス Neural Engine",
        "tech_1_desc": "すべてのパズル生成と物理シミュレーションは端末内のチップで完結。外部通信ゼロ、完全なプライバシー保護。",
        "tech_2_title": "TrueDepth 視線集中ガイダンス",
        "tech_2_desc": "TrueDepth カメラにより視線の安定度を測定し、環境光と木香の環境音を優しく調和させ、没入感を高めます。",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "心拍変動 (HRV) をローカルで取得し、パズル挑戦前後の自律神経リラックス度と集中フローを可視化します。",
        "tech_4_title": "432Hz 東洋五音メディテーション",
        "tech_4_desc": "古琴、編鐘、深山の雨音、そして心地よい触覚フィードバックが、五感に響く深い癒しをお届けします。",
        "tiers_heading": "匠の収蔵メンバーシップ",
        "tiers_sub": "Apple StoreKit 2 による安心の決済管理。Apple ID 設定からいつでも解約可能。",
        "tier_1_title": "月額練習プラン",
        "tier_1_badge": "柔軟な月額サブスクリプション · いつでも管理可能",
        "tier_1_feature_1": "すべての3D魯班ロック＆2D燕幾図の上級ステージを解放",
        "tier_1_feature_2": "朝の集中と夜の癒しをもたらす東洋の伝統サウンドセラピー",
        "tier_1_feature_3": "タッチの滑らかさと集中度のマインドフルネス分析レポート",
        "tier_2_title": "年間フロープラン (主に推奨)",
        "tier_2_badge": "無料体験付き · App Storeの特別オファーに準拠",
        "tier_2_feature_1": "五千年の文明絵巻と最高難度の名匠からくりを完全体験",
        "tier_2_feature_2": "端末内AIによる無限の仕口・盤面自動生成工房を解放",
        "tier_2_feature_3": "TrueDepth視線追跡＆Apple Watch HRV心流レポート",
        "tier_2_feature_4": "無制限の天灯祈願儀礼＆10言語対応の風雅な灯謎クイズ",
        "tier_3_title": "生涯コレクターパス",
        "tier_3_badge": "和田青玉印章の落款特権 · 永久アンロック",
        "tier_3_feature_1": "一度のお支払いで、全章節と将来のすべてのアップデートを永久保有",
        "tier_3_feature_2": "限定の「生涯コレクター和田青玉印章」刻印特権",
        "tier_3_feature_3": "将来の Apple Vision Pro 空間巨大機構拡張パックを含む",
        "tier_3_feature_4": "サブスクリプションの重圧なし。静寂な東洋工芸デジタル美術館を永遠に手元に",
        "eula_disclosure_title": "App Store 自動更新サブスクリプション利用条件",
        "eula_disclosure_text": "購入確定時にお客様の Apple ID アカウントに請求されます。現在の請求期間が終了する少なくとも24時間前までにキャンセルしない限り、サブスクリプションは自動的に更新されます。終了前の24時間以内に更新料金が請求されます。購入後、Apple ID アカウント設定にていつでもサブスクリプションの管理および解約が可能です。",
        "footer_rights": "著作権所有 © 2026 心象天工 MindCraft Zen チーム。全著作権所有。",
        "footer_privacy": "プライバシーポリシー",
        "footer_eula": "Apple 標準使用許諾契約 (Standard EULA)",
        "footer_support": "お問い合わせ・サポート：howly7777777@gmail.com",
    },
    "ko": {
        "nav_title": "심상천공",
        "nav_subtitle": "MindCraft Zen",
        "nav_crafts": "4대 전통기구",
        "nav_tech": "선(禪) 테크놀로지",
        "nav_tiers": "장인 소장권",
        "nav_privacy": "개인정보 처리방침",
        "nav_terms": "이용약관 (EULA)",
        "nav_support": "✉️ 고객지원",
        "footer_support_label": "공식 고객지원 및 문의 이메일",
        "hero_badge": "5000년 전통 목공 퍼즐 · 온디바이스 AI 집중력 스튜디오",
        "hero_title": "심상천공 · 목구조와 선(禪)",
        "hero_subtitle": "3D 노반쇄, 2D 송대 연기재, 구연환, 낙서 화용도에 몰입하세요. 장부맞춤의 맑은 울림 속에서 내면의 평온과 깊은 집중을 회복합니다.",
        "hero_cta": "App Store 에서 다운로드",
        "hero_cta_sub": "iPhone, iPad 및 Apple Vision Pro 지원",
        "crafts_heading": "5000년 동양의 지혜 · 4대 목공 결합 및 위상 기구",
        "crafts_sub": "못이나 접착제를 전혀 사용하지 않고 오직 공간 위상과 2진법 그레이 코드의 조화로 완성됩니다.",
        "craft_1_title": "3D 노반쇄 (공명쇄)",
        "craft_1_desc": "3차원 공간에서 360도 자유롭게 회전하며 분해. 못 하나 없이 천 근의 무게를 지탱하는 동양의 공간 구조 철학을 체험합니다.",
        "craft_2_title": "2D 송대 연기재 (칠교의 조상)",
        "craft_2_desc": "남송 황백사의 연회 탁자 도면. 가구의 이합집산을 통해 송대 문인들의 고아한 심미안과 다차원 공간 기하학을 즐깁니다.",
        "craft_3_title": "천도 구연환",
        "craft_3_desc": "옥 고리와 금 비녀의 정교한 결합. 2진법 그레이 코드의 순환 천률을 담아 고리를 풀 때마다 마음을 차분히 가라앉힙니다.",
        "craft_4_title": "낙서 화용도",
        "craft_4_desc": "음양의 기정을 배치한 구궁 수리. 좁은 판 위에서 지혜를 모아 포위를 뚫고 동양 고대 병법의 전략을 경험합니다.",
        "tech_heading": "순수한 몰입의 경지 · 최첨단 Apple 기술",
        "tech_sub": "깊은 마음챙김을 위해 설계되었습니다. 광고 제로, 외부 데이터 수집 제로.",
        "tech_1_title": "100% 온디바이스 Neural Engine",
        "tech_1_desc": "모든 퍼즐 생성과 물리 연산이 기기 내부 칩에서 안전하게 실행됩니다. 인터넷 연결 불필요, 외부 서버 업로드 제로.",
        "tech_2_title": "TrueDepth 시선 집중 추적",
        "tech_2_desc": "전면 TrueDepth 카메라로 응시 안정성을 실시간 감지하여 조명과 명상 사운드를 최적화하고 몰입을 돕습니다.",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "심박변이도(HRV)를 로컬에서 연동하여 퍼즐 풀이 전후 자율신경계 이완 지수와 몰입도를 분석합니다.",
        "tech_4_title": "432Hz 동양 전통 명상 음향",
        "tech_4_desc": "천년 고금, 편경, 산속 빗소리 및 실감나는 목재 햅틱 진동이 오감에 깊은 위안을 선사합니다.",
        "tiers_heading": "장인 소장권 멤버십",
        "tiers_sub": "Apple StoreKit 2 기반의 안전한 결제. Apple ID 설정에서 언제든 자유롭게 해지 가능.",
        "tier_1_title": "월간 수양 플랜",
        "tier_1_badge": "유연한 월간 구독 · 언제든 해지 가능",
        "tier_1_feature_1": "모든 3D 노반쇄 및 2D 연기재 고급 스테이지 해금",
        "tier_1_feature_2": "아침 집중 및 밤의 안식을 위한 동양 사운드 테라피",
        "tier_1_feature_3": "터치 유연성 및 마음챙김 집중도 분석 보고서",
        "tier_2_title": "연간 몰입 플랜 (추천)",
        "tier_2_badge": "무료 체험 포함 · App Store 혜택 연동",
        "tier_2_feature_1": "5000년 역사 두루마리와 최고 난도 명인 기구 전체 체험",
        "tier_2_feature_2": "온디바이스 AI 무한 장부맞춤 및 엔드게임 퍼즐 공방 해금",
        "tier_2_feature_3": "고급 TrueDepth 시선 추적 & Apple Watch HRV 몰입 보고서",
        "tier_2_feature_4": "무제한 풍등 띄우기 소원 의식 및 10개 언어 등불 수수께끼",
        "tier_3_title": "평생 소장자 패스",
        "tier_3_badge": "호탄청옥 인장 특권 · 영구 해금",
        "tier_3_feature_1": "단 1회 결제로 모든 챕터와 향후 업데이트 영구 소장",
        "tier_3_feature_2": "독점 '평생 소장자 호탄청옥 인장' 낙관 특권",
        "tier_3_feature_3": "향후 Apple Vision Pro 공간 거대 기구 확장팩 포함",
        "tier_3_feature_4": "구독 부담 제로. 고요한 디지털 동양 공예 박물관을 소장하세요",
        "eula_disclosure_title": "App Store 자동 갱신 구독 약관 안내",
        "eula_disclosure_text": "결제는 구매 확인 시 Apple ID 계정으로 청구됩니다. 현재 기간이 종료되기 최소 24시간 전에 취소하지 않으면 구독이 자동으로 갱신됩니다. 현재 기간 종료 전 24시간 이내에 갱신 비용이 계정으로 청구됩니다. 구매 후 Apple ID 계정 설정에서 언제든지 구독을 관리하거나 취소할 수 있습니다.",
        "footer_rights": "Copyright © 2026 심상천공 MindCraft Zen 팀. All rights reserved.",
        "footer_privacy": "개인정보 처리방침",
        "footer_eula": "Apple 표준 라이선스 계약 (Standard EULA)",
        "footer_support": "고객지원 문의: howly7777777@gmail.com",
    },
    "de": {
        "nav_title": "MindCraft Zen",
        "nav_subtitle": "Holzmechanik & Zen",
        "nav_crafts": "4 Antike Künste",
        "nav_tech": "Zen-Technologie",
        "nav_tiers": "Mitgliedschaft",
        "nav_privacy": "Datenschutz",
        "nav_terms": "Nutzungsbedingungen (EULA)",
        "nav_support": "✉️ Support",
        "footer_support_label": "Offizieller Support & Kontakt",
        "hero_badge": "5.000 Jahre chinesische Holzmechanik · Lokales KI-Studio",
        "hero_title": "MindCraft Zen · Holzmechanik & Geist",
        "hero_subtitle": "Tauchen Sie ein in 3D-Luban-Schlösser, 2D-Yanji-Tische, die Neun Verketteten Ringe und das Klotski-Puzzle. Finden Sie tiefe Ruhe und Fokus im Klang präziser Holzverbindungen.",
        "hero_cta": "Im App Store laden",
        "hero_cta_sub": "Für iPhone, iPad und Apple Vision Pro",
        "crafts_heading": "5.000 Jahre Erbe · 4 Meisterhafte Holzmechanik-Künste",
        "crafts_sub": "Ohne Nägel, ohne Leim. Reine Raumtopologie, binäre Rekursion und orientalische Ausgewogenheit.",
        "craft_1_title": "3D-Luban-Schloss (Kongming-Schloss)",
        "craft_1_desc": "Dreidimensionale Raumgeometrie. 360-Grad-Rotation zur Demontage jahrhundertealter chinesischer Zapfenverbindungen.",
        "craft_2_title": "2D-Yanji-Tische (Ahne des Tangrams)",
        "craft_2_desc": "Huang Bosis Bankett-Arrangements aus der südlichen Song-Dynastie. Elegante geometrische Holzkompositionen.",
        "craft_3_title": "Himmlische Neun Verkettete Ringe",
        "craft_3_desc": "Jade-Ringe an doppelter Haarnadel. Basierend auf dem binären Gray-Code führt jeder Schritt zu innerer Klarheit.",
        "craft_4_title": "Luoshu-Klotski-Schiebepuzzle",
        "craft_4_desc": "Neun-Paläste-Kosmologie trifft auf historische Taktik. Manövrieren Sie durch engste Pfade zum strategischen Durchbruch.",
        "tech_heading": "Reine Zen-Ruhe · Wegweisende Apple-Technologie",
        "tech_sub": "Entwickelt für tiefen Fokus. Werbefrei, absolut privat und ohne Datenweitergabe.",
        "tech_1_title": "100% Lokale Apple Neural Engine",
        "tech_1_desc": "Alle Puzzle-Berechnungen laufen direkt auf Ihrem Gerät. Keine Internetverbindung erforderlich, keine Cloud-Uploads.",
        "tech_2_title": "TrueDepth-Blickfokus-Führung",
        "tech_2_desc": "Erfasst sanft die Blickstabilität über die Frontkamera, um Beleuchtung und Klang optimal an Ihre Konzentration anzupassen.",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "Misst Ihre Herzfrequenzvariabilität (HRV) lokal, um die Entspannung vor und nach jeder Session sichtbar zu machen.",
        "tech_4_title": "432Hz Orientalische Klangwelten",
        "tech_4_desc": "Meisterhafte Guqin-Harmonien, Glockenklänge und haptisches Holz-Feedback schaffen vollkommene sensorische Harmonie.",
        "tiers_heading": "Meister-Pass Mitgliedschaft",
        "tiers_sub": "Verwaltet über Apple StoreKit 2. Transparent und jederzeit in den Apple-ID-Einstellungen kündbar.",
        "tier_1_title": "Monatlicher Übungsplan",
        "tier_1_badge": "Flexibles Monatsabo · Jederzeit kündbar",
        "tier_1_feature_1": "Alle 3D-Luban-Schlösser & 2D-Yanji-Meisterstufen freischalten",
        "tier_1_feature_2": "Morgendliche Fokussierung & abendliche orientalische Klangtherapie",
        "tier_1_feature_3": "Touch-Flüssigkeit & Achtsamkeits-Konzentrationsanalyse",
        "tier_2_title": "Jährlicher Ablaufplan (Empfohlen)",
        "tier_2_badge": "Inklusive kostenloser Testphase · Nach App Store Angebot",
        "tier_2_feature_1": "Vollständiger Zugang zu 5.000 Jahren Geschichte & Großmeister-Rätseln",
        "tier_2_feature_2": "On-Device KI-Werkstatt für unendliche Zapfen- und Endspiel-Rätsel",
        "tier_2_feature_3": "Erweiterte TrueDepth-Blickstabilität & Apple Watch HRV-Berichte",
        "tier_2_feature_4": "Unbegrenzte Himmelslaternen-Rituale & 10-Sprachen-Laternenrätsel",
        "tier_3_title": "Lebenslanger Sammler-Pass",
        "tier_3_badge": "Hetian-Jade-Sammlersiegel · Dauerhafte Freischaltung",
        "tier_3_feature_1": "Einmalzahlung für dauerhaften Zugriff auf alle Kapitel und zukünftige Updates",
        "tier_3_feature_2": "Exklusives Sammler-Privileg mit Hetian-Jade-Siegel",
        "tier_3_feature_3": "Beinhaltet zukünftiges Apple Vision Pro Raummechanik-Erweiterungspaket",
        "tier_3_feature_4": "Kein Abonnement-Druck. Sammeln Sie ein ruhiges digitales Kunstmuseum",
        "eula_disclosure_title": "App Store Bedingungen für automatische Verlängerung",
        "eula_disclosure_text": "Die Zahlung wird bei Kaufbestätigung über Ihr Apple-ID-Konto abgerechnet. Das Abonnement verlängert sich automatisch, sofern es nicht mindestens 24 Stunden vor Ablauf des aktuellen Zeitraums gekündigt wird. Die Verlängerungsgebühr wird innerhalb von 24 Stunden vor Ende des laufenden Zeitraums fällig. Sie können Ihr Abonnement jederzeit in Ihren Apple-ID-Kontoeinstellungen verwalten oder kündigen.",
        "footer_rights": "Copyright © 2026 MindCraft Zen Team. Alle Rechte vorbehalten.",
        "footer_privacy": "Datenschutzerklärung",
        "footer_eula": "Apple Standard EULA",
        "footer_support": "Support & Kontakt: howly7777777@gmail.com",
    },
    "fr": {
        "nav_title": "MindCraft Zen",
        "nav_subtitle": "Art du Bois & Zen",
        "nav_crafts": "4 Arts Anciens",
        "nav_tech": "Technologie Zen",
        "nav_tiers": "Abonnement",
        "nav_privacy": "Confidentialité",
        "nav_terms": "Conditions d'utilisation (EULA)",
        "nav_support": "✉️ Assistance",
        "footer_support_label": "Assistance officielle & Contact",
        "hero_badge": "5 000 ans d'artisanat oriental · Studio de concentration IA locale",
        "hero_title": "MindCraft Zen · Assemblage & Esprit",
        "hero_subtitle": "Plongez dans les verrous 3D de Luban, les tables 2D Yanji des Song, les Neuf Anneaux et le Klotski. Retrouvez calme et clarté d'esprit dans le son pur du bois emboîté.",
        "hero_cta": "Télécharger sur l'App Store",
        "hero_cta_sub": "Conçu pour iPhone, iPad et Apple Vision Pro",
        "crafts_heading": "5 000 ans d'héritage · 4 chefs-d'œuvre d'assemblage",
        "crafts_sub": "Ni clou ni colle. Pure topologie spatiale, récursion binaire et équilibre ancestral.",
        "craft_1_title": "Verrou 3D de Luban (Kongming)",
        "craft_1_desc": "Géométries célestes et tenons ancestraux. Faites pivoter à 360° pour percer les secrets des bâtisseurs chinois sans le moindre clou.",
        "craft_2_title": "Tables 2D Yanji (Ancêtre du Tangram)",
        "craft_2_desc": "Le traité de banquet de Huang Bosi sous la dynastie Song du Sud. Agencez les tables de bois pour explorer la géométrie spatiale des lettrés.",
        "craft_3_title": "Les Neuf Anneaux Célestes",
        "craft_3_desc": "Anneaux de jade blanc et épingle d'or. Incarnant le code Gray binaire, chaque mouvement guide l'esprit vers une quiétude infinie.",
        "craft_4_title": "Casse-tête Klotski Luoshu",
        "craft_4_desc": "La cosmologie des neuf palais alliée à la tactique militaire antique. Déplacez les pièces pour ouvrir le passage stratégique.",
        "tech_heading": "Sanctuaire Zen Pur · Technologie Apple Avancée",
        "tech_sub": "Créé pour un état de flow profond. Sans publicité, sans suivi, respect absolu de votre vie privée.",
        "tech_1_title": "100% Neural Engine sur l'appareil",
        "tech_1_desc": "Tous les calculs et la génération d'énigmes s'exécutent directement sur la puce de votre appareil, sans connexion réseau.",
        "tech_2_title": "Guidage visuel TrueDepth",
        "tech_2_desc": "Mesure en direct la stabilité du regard pour harmoniser subtilement l'ambiance lumineuse et sonore de votre atelier.",
        "tech_3_title": "Apple Watch & HealthKit VRC",
        "tech_3_desc": "Analyse locale de la variabilité de la fréquence cardiaque (VRC) pour mesurer votre relaxation avant et après chaque session.",
        "tech_4_title": "Paysages sonores orientaux 432Hz",
        "tech_4_desc": "Accords de Guqin, résonances de cloches antiques et retours haptiques réalistes pour une harmonie sensorielle totale.",
        "tiers_heading": "Abonnements Artisan Privilège",
        "tiers_sub": "Gestion sécurisée via Apple StoreKit 2. Annulation facile à tout moment dans vos réglages Apple ID.",
        "tier_1_title": "Pratique Mensuelle",
        "tier_1_badge": "Abonnement mensuel flexible · Gestion à tout moment",
        "tier_1_feature_1": "Débloquez tous les verrous 3D de Luban et tables Yanji 2D",
        "tier_1_feature_2": "Méditation matinale et thérapie sonore orientale du soir",
        "tier_1_feature_3": "Rapport de fluidité tactile et d'attention en pleine conscience",
        "tier_2_title": "Immersion Annuelle (Recommandée)",
        "tier_2_badge": "Essai gratuit inclus · Selon l'offre App Store",
        "tier_2_feature_1": "Accès intégral à la fresque historique de 5 000 ans et casse-têtes maîtres",
        "tier_2_feature_2": "Atelier IA local avec génération infinie d'assemblages et de fins de partie",
        "tier_2_feature_3": "Suivi du regard TrueDepth et rapport de flow VRC Apple Watch",
        "tier_2_feature_4": "Lâcher illimité de lanternes célestes et énigmes en 10 langues",
        "tier_3_title": "Pass Collectionneur à Vie",
        "tier_3_badge": "Sceau en jade de Hetian · Déblocage permanent",
        "tier_3_feature_1": "Paiement unique pour un accès perpétuel à tous les chapitres et mises à jour",
        "tier_3_feature_2": "Privilège exclusif de signature au sceau en jade de Hetian",
        "tier_3_feature_3": "Inclut la future extension spatiale Apple Vision Pro",
        "tier_3_feature_4": "Zéro pression d'abonnement. Collectionnez un musée d'artisanat numérique",
        "eula_disclosure_title": "Conditions d'abonnement auto-renouvelable App Store",
        "eula_disclosure_text": "Le paiement est débité de votre compte Apple ID à la confirmation d'achat. L'abonnement se renouvelle automatiquement sauf résiliation au moins 24 heures avant la fin de la période en cours. Votre compte sera débité dans les 24 heures précédant la fin de la période en cours. Vous pouvez gérer et annuler vos abonnements dans les réglages de votre compte App Store après l'achat.",
        "footer_rights": "Copyright © 2026 Équipe MindCraft Zen. Tous droits réservés.",
        "footer_privacy": "Politique de confidentialité",
        "footer_eula": "Contrat de licence standard Apple (EULA)",
        "footer_support": "Assistance & Contact : howly7777777@gmail.com",
    },
    "es": {
        "nav_title": "MindCraft Zen",
        "nav_subtitle": "Sabiduría y Zen",
        "nav_crafts": "4 Artes Antiguas",
        "nav_tech": "Tecnología Zen",
        "nav_tiers": "Membresía",
        "nav_privacy": "Privacidad",
        "nav_terms": "Términos de uso (EULA)",
        "nav_support": "✉️ Soporte",
        "footer_support_label": "Soporte oficial y Contacto",
        "hero_badge": "5.000 años de artesanía oriental · Estudio de enfoque con IA local",
        "hero_title": "MindCraft Zen · Ensamblaje y Mente",
        "hero_subtitle": "Sumérgete en los cerrojos 3D de Luban, las mesas 2D Yanji de la dinastía Song, los Nueve Anillos y el Klotski. Encuentra calma y claridad mental con el crujido de la madera ensamblada.",
        "hero_cta": "Descargar en el App Store",
        "hero_cta_sub": "Diseñado para iPhone, iPad y Apple Vision Pro",
        "crafts_heading": "5.000 años de legado · 4 obras maestras de ensamble",
        "crafts_sub": "Sin clavos ni pegamento. Pura topología espacial, recursión binaria y equilibrio atemporal.",
        "craft_1_title": "Cerrojo 3D de Luban (Kongming)",
        "craft_1_desc": "Geometría espacial milenaria. Gira libremente en 3D para desarmar ensambles tradicionales que resisten toneladas sin un solo clavo.",
        "craft_2_title": "Mesas 2D Yanji (Origen del Tangram)",
        "craft_2_desc": "El tratado de banquetes de Huang Bosi en la dinastía Song del Sur. Modifica mesas geométricas para explorar la estética espacial clásica.",
        "craft_3_title": "Nueve Anillos Celestiales",
        "craft_3_desc": "Anillos de jade y horquilla dorada. Basado en el código binario Gray, cada paso guía la mente hacia una profunda serenidad.",
        "craft_4_title": "Rompecabezas Klotski Luoshu",
        "craft_4_desc": "Cosmología de los nueve palacios y táctica militar histórica. Maniobra en espacios estrechos para lograr el escape maestro.",
        "tech_heading": "Puro Santuario Zen · Tecnología Apple de Vanguardia",
        "tech_sub": "Diseñado para un flujo de concentración profundo. Sin anuncios, con total privacidad.",
        "tech_1_title": "100% Neural Engine en el dispositivo",
        "tech_1_desc": "Todos los rompecabezas y cálculos se procesan directamente en el chip de tu dispositivo. Cero conexión obligatoria, cero envíos a la nube.",
        "tech_2_title": "Guía de mirada TrueDepth",
        "tech_2_desc": "Detecta en vivo la estabilidad de tu mirada con la cámara frontal para regular la iluminación y el sonido ambiente de tu sesión.",
        "tech_3_title": "Apple Watch & HealthKit VFC",
        "tech_3_desc": "Monitorea tu variabilidad de la frecuencia cardíaca (VFC) de forma local para reflejar la calma antes y después de resolver cada reto.",
        "tech_4_title": "Sonidos orientales en 432Hz",
        "tech_4_desc": "Acordes de Guqin, campanas ceremoniales y vibración háptica realista para una armonía sensorial insuperable.",
        "tiers_heading": "Membresías de Artesano",
        "tiers_sub": "Gestionado con Apple StoreKit 2. Transparente y cancelable en cualquier momento desde los ajustes de tu Apple ID.",
        "tier_1_title": "Plan de Práctica Mensual",
        "tier_1_badge": "Suscripción mensual flexible · Cancela cuando quieras",
        "tier_1_feature_1": "Desbloquea todos los cerrojos 3D de Luban y mesas 2D Yanji",
        "tier_1_feature_2": "Sonoterapia matutina y nocturna para serenar la mente",
        "tier_1_feature_3": "Reporte de fluidez táctil y concentración plena",
        "tier_2_title": "Plan de Flujo Anual (Recomendado)",
        "tier_2_badge": "Prueba gratis incluida · Sincronizado con App Store",
        "tier_2_feature_1": "Acceso total a los 5.000 años de historia y acertijos de grandes maestros",
        "tier_2_feature_2": "Taller con IA local para ensambles y finales de partida infinitos",
        "tier_2_feature_3": "Seguimiento de mirada TrueDepth y reporte de flujo con Apple Watch",
        "tier_2_feature_4": "Lanzamiento ilimitado de linternas voladoras y acertijos en 10 idiomas",
        "tier_3_title": "Pase de Coleccionista de por Vida",
        "tier_3_badge": "Sello de jade de Hetian · Desbloqueo permanente",
        "tier_3_feature_1": "Pago único para acceso perpetuo a todos los capítulos y futuras mejoras",
        "tier_3_feature_2": "Privilegio exclusivo de estampación con sello de jade de Hetian",
        "tier_3_feature_3": "Incluye la futura expansión espacial para Apple Vision Pro",
        "tier_3_feature_4": "Sin cuotas mensuales. Colecciona un museo de arte oriental digital",
        "eula_disclosure_title": "Términos de suscripción autorrenovable del App Store",
        "eula_disclosure_text": "El pago se cargará a tu cuenta de Apple ID al confirmar la compra. La suscripción se renueva automáticamente a menos que se cancele al menos 24 horas antes del final del período actual. La renovación se cobrará en las 24 horas previas al término del período en curso. Puedes gestionar y cancelar tus suscripciones en los ajustes de tu cuenta del App Store tras la compra.",
        "footer_rights": "Copyright © 2026 Equipo MindCraft Zen. Todos los derechos reservados.",
        "footer_privacy": "Política de Privacidad",
        "footer_eula": "Acuerdo de Licencia Estándar de Apple (EULA)",
        "footer_support": "Soporte y Contacto: howly7777777@gmail.com",
    },
    "vi": {
        "nav_title": "Tâm Tượng Thiên Công",
        "nav_subtitle": "MindCraft Zen",
        "nav_crafts": "Tứ Đại Cổ Trí",
        "nav_tech": "Thiền Định Công Nghệ",
        "nav_tiers": "Bộ Sưu Tập Nghệ Nhân",
        "nav_privacy": "Chính Sách Quyền Riêng Tư",
        "nav_terms": "Điều Khoản Sử Dụng (EULA)",
        "nav_support": "✉️ Hỗ trợ",
        "footer_support_label": "Hỗ trợ chính thức & Liên hệ",
        "hero_badge": "Cơ quan mộng mộng 5000 năm · Không gian thiền định AI cục bộ Apple",
        "hero_title": "Tâm Tượng Thiên Công · Mộc Cấu & Thiền",
        "hero_subtitle": "Đắm mình trong Khóa Lỗ Ban 3D, Yến Kỷ Đồ thời Tống 2D, Cửu Liên Hoàn và Hoa Dung Đạo. Tìm lại sự an yên và tập trung sâu sắc trong tiếng lách cách của mộng gỗ ăn khớp.",
        "hero_cta": "Tải về trên App Store",
        "hero_cta_sub": "Tương thích iPhone, iPad và Apple Vision Pro",
        "crafts_heading": "5.000 năm di sản phương Đông · Tứ đại cơ quan mộng ghép",
        "crafts_sub": "Không dùng một chiếc đinh hay giọt keo nào. Hoàn toàn dựa vào hình học không gian và quy luật nhị phân.",
        "craft_1_title": "Khóa Lỗ Ban 3D (Khổng Minh Tỏa)",
        "craft_1_desc": "Lục tử liên phương, bát giác càn khôn. Xoay 360 độ trong không gian 3 chiều để tháo lắp trí tuệ mộng ngàm ngàn năm chịu lực vững chãi.",
        "craft_2_title": "Yến Kỷ Đồ Thời Tống 2D (Tổ của Tangram)",
        "craft_2_desc": "Phổ bàn tiệc yến của Hoàng Bá Tư thời Nam Tống. Hoán đổi bàn gỗ hình học để cảm nhận thẩm mỹ thanh tao và nghệ thuật không gian.",
        "craft_3_title": "Thiên Đạo Cửu Liên Hoàn",
        "craft_3_desc": "Vòng ngọc đan xen cùng trâm vàng đôi. Mang mã Gray nhị phân đệ quy tuần hoàn, mỗi vòng tháo ra đưa tâm trí vào tĩnh lặng vô biên.",
        "craft_4_title": "Hoa Dung Đạo Lạc Thư",
        "craft_4_desc": "Âm dương phối hợp, cửu cung biến hóa. Vận dụng mưu lược trên bàn cờ tấc vuông để mở đường đột phá trong thế trận xưa.",
        "tech_heading": "Không Gian Thiền Thuần Khiết · Công Nghệ Tiên Tiến Apple",
        "tech_sub": "Được thiết kế cho trạng thái tập trung sâu. Không quảng cáo, hoàn toàn riêng tư.",
        "tech_1_title": "100% Neural Engine Cục Bộ",
        "tech_1_desc": "Mọi thuật toán tạo câu đố và xử lý vật lý chạy hoàn toàn trên chip thiết bị của bạn. Không cần internet, không tải dữ liệu lên máy chủ.",
        "tech_2_title": "Theo Dõi Ánh Mắt TrueDepth",
        "tech_2_desc": "Đo độ ổn định của ánh nhìn qua camera TrueDepth để tinh chỉnh ánh sáng và âm thanh mộc, giúp bạn tập trung tuyệt đối.",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "Đọc độ biến thiên nhịp tim (HRV) cục bộ để hiển thị chỉ số thư giãn thần kinh và dòng chảy tập trung trước và sau khi giải đố.",
        "tech_4_title": "Âm Thanh Thiền Phương Đông 432Hz",
        "tech_4_desc": "Hợp âm Cổ Cầm, chuông khánh, mưa rào trên núi cùng phản hồi rung xúc giác chân thực mang lại sự an yên toàn diện.",
        "tiers_heading": "Gói Hội Viên Nghệ Nhân",
        "tiers_sub": "Quản lý minh bạch qua Apple StoreKit 2. Hủy bất cứ lúc nào trong Cài đặt Apple ID của bạn.",
        "tier_1_title": "Kế Hoạch Tu Tập Hàng Tháng",
        "tier_1_badge": "Đăng ký hàng tháng linh hoạt · Quản lý bất kỳ lúc nào",
        "tier_1_feature_1": "Mở khóa toàn bộ Khóa Lỗ Ban 3D và Yến Kỷ Đồ 2D cấp cao",
        "tier_1_feature_2": "Trị liệu âm thanh phương Đông cho buổi sáng và đêm muộn",
        "tier_1_feature_3": "Báo cáo phân tích độ mượt mà khi chạm và khả năng tập trung",
        "tier_2_title": "Kế Hoạch Dòng Chảy Hàng Năm (Khuyên Dùng)",
        "tier_2_badge": "Bao gồm dùng thử miễn phí · Theo ưu đãi App Store",
        "tier_2_feature_1": "Trải nghiệm trọn vẹn cuộn sử 5000 năm và các cơ quan đại sư",
        "tier_2_feature_2": "Xưởng AI cục bộ tạo mộng gỗ vô tận và thế cờ tàn",
        "tier_2_feature_3": "Theo dõi ánh mắt TrueDepth và báo cáo dòng chảy HRV Apple Watch",
        "tier_2_feature_4": "Thả đèn trời cầu phúc không giới hạn và câu đố đèn lồng 10 thứ tiếng",
        "tier_3_title": "Thẻ Nhà Sưu Tập Trọn Đời",
        "tier_3_badge": "Tặng ấn ngọc Hòa Điền · Mở khóa vĩnh viễn",
        "tier_3_feature_1": "Thanh toán một lần, sở hữu vĩnh viễn tất cả chương và bản cập nhật",
        "tier_3_feature_2": "Đặc quyền khắc ấn chương ngọc bích Hòa Điền của nhà sưu tập",
        "tier_3_feature_3": "Bao gồm gói mở rộng cơ quan không gian Apple Vision Pro tương lai",
        "tier_3_feature_4": "Không áp lực đăng ký định kỳ. Lưu giữ một bảo tàng thủ công mỹ nghệ số",
        "eula_disclosure_title": "Điều Khoản Đăng Ký Tự Động Gia Hạn App Store",
        "eula_disclosure_text": "Thanh toán sẽ được tính vào tài khoản Apple ID của bạn khi xác nhận mua. Đăng ký sẽ tự động gia hạn trừ khi bị hủy ít nhất 24 giờ trước khi kết thúc kỳ hiện tại. Tài khoản sẽ bị tính phí gia hạn trong vòng 24 giờ trước khi kết thúc kỳ hiện tại. Bạn có thể quản lý và hủy đăng ký trong cài đặt tài khoản App Store bất cứ lúc nào sau khi mua.",
        "footer_rights": "Bản quyền © 2026 Đội ngũ MindCraft Zen. Bảo lưu mọi quyền.",
        "footer_privacy": "Chính Sách Quyền Riêng Tư",
        "footer_eula": "Thỏa Thuận Cấp Phép Tiêu Chuẩn của Apple (EULA)",
        "footer_support": "Hỗ trợ & Liên hệ: howly7777777@gmail.com",
    },
    "th": {
        "nav_title": "MindCraft Zen",
        "nav_subtitle": "กลไกไม้และสมาธิ",
        "nav_crafts": "4 สุดยอดกลไก",
        "nav_tech": "เทคโนโลยีเซน",
        "nav_tiers": "สมาชิกงานฝีมือ",
        "nav_privacy": "นโยบายความเป็นส่วนตัว",
        "nav_terms": "ข้อกำหนดการใช้งาน (EULA)",
        "nav_support": "✉️ ฝ่ายสนับสนุน",
        "footer_support_label": "ฝ่ายสนับสนุนและติดต่ออย่างเป็นทางการ",
        "hero_badge": "ภูมิปัญญาตะวันออก 5,000 ปี · สตูดิโอฝึกสมาธิด้วย AI บนอุปกรณ์ Apple",
        "hero_title": "MindCraft Zen · กลไกไม้และจิตวิญญาณ",
        "hero_subtitle": "ดื่มด่ำกับตัวล็อกหลู่ปาน 3 มิติ, ผังโต๊ะเยี่ยนจีสมัยซ่ง 2 มิติ, ห่วงเก้าประสาน และกลศึกฮวาหรงเต้า ค้นพบความสงบในใจผ่านเสียงประกอบไม้สลักอันประณีต",
        "hero_cta": "ดาวน์โหลดบน App Store",
        "hero_cta_sub": "ออกแบบมาสำหรับ iPhone, iPad และ Apple Vision Pro",
        "crafts_heading": "มรดกตกทอด 5,000 ปี · 4 สุดยอดงานช่างไม้โบราณ",
        "crafts_sub": "ไม่ใช้ตะปูแม้แต่ตัวเดียว ไม่พึ่งพากาว ใช้เพียงรูปทรงเรขาคณิตและรหัสเกรย์แห่งธรรมชาติ",
        "craft_1_title": "ตัวล็อกหลู่ปาน 3 มิติ (ล็อกขงเบ้ง)",
        "craft_1_desc": "หมุนสำรวจ 360 องศาในแบบ 3 มิติ สัมผัสปรัชญาช่างไม้ตะวันออกที่รับน้ำหนักมหาศาลได้โดยไม่ต้องใช้ตะปู",
        "craft_2_title": "ผังโต๊ะเยี่ยนจี 2 มิติ (ต้นกำเนิดแทนแกรม)",
        "craft_2_desc": "ตำราโต๊ะจัดเลี้ยงของหวงป๋อซือสมัยราชวงศ์ซ่งใต้ เรียงโต๊ะเรขาคณิตเพื่อสัมผัสสุนทรียศาสตร์ของบัณฑิตโบราณ",
        "craft_3_title": "ห่วงเก้าประสานสวรรค์",
        "craft_3_desc": "ห่วงหยกและปิ่นปักผมคู่ ถักทอรหัสเกรย์ทวิภาคอย่างลึกซึ้ง ทุกการปลดห่วงช่วยให้จิตใจสงบนิ่งและมีสมาธิ",
        "craft_4_title": "กลกระดานฮวาหรงเต้า",
        "craft_4_desc": "ผสานหยินหยางและแผนผังเก้าช่อง ขยับเบี้ยในตารางแคบเพื่อเปิดทางหลบหนีตามยุทธศาสตร์สงครามโบราณ",
        "tech_heading": "วิถีเซนอันบริสุทธิ์ · เทคโนโลยีชั้นนำจาก Apple",
        "tech_sub": "ออกแบบเพื่อสมาธิขั้นสูง ปราศจากโฆษณา ไม่มีการเก็บข้อมูลส่วนบุคคล",
        "tech_1_title": "Neural Engine บนอุปกรณ์ 100%",
        "tech_1_desc": "การคำนวณและสร้างปริศนาทั้งหมดทำงานบนชิปของอุปกรณ์โดยตรง ไม่จำเป็นต้องเชื่อมต่ออินเทอร์เน็ต ไม่ส่งข้อมูลขึ้นคลาวด์",
        "tech_2_title": "ตรวจจับสายตาด้วย TrueDepth",
        "tech_2_desc": "ใช้กล้อง TrueDepth ตรวจวัดความนิ่งของสายตาแบบเรียลไทม์ ปรับแสงและเสียงบรรยากาศเพื่อช่วยให้คุณจดจ่อได้ดีที่สุด",
        "tech_3_title": "Apple Watch & HealthKit HRV",
        "tech_3_desc": "อ่านค่าความผันแปรของอัตราการเต้นของหัวใจ (HRV) เพื่อแสดงระดับความผ่อนคลายของระบบประสาทก่อนและหลังการเล่น",
        "tech_4_title": "เสียงสมาธิ 432Hz สไตล์ตะวันออก",
        "tech_4_desc": "เสียงพิณกู่ฉิน ระฆังโบราณ เสียงฝนตกในป่าลึก และระบบสั่นสัมผัสเสมือนจริงเพื่อความสงบผ่อนคลายรอบด้าน",
        "tiers_heading": "แพ็กเกจสมาชิกช่างฝีมือ",
        "tiers_sub": "จัดการอย่างปลอดภัยผ่าน Apple StoreKit 2 ยกเลิกได้ตลอดเวลาในการตั้งค่า Apple ID ของคุณ",
        "tier_1_title": "แผนฝึกสมาธิรายเดือน",
        "tier_1_badge": "สมัครรายเดือนแบบยืดหยุ่น · จัดการได้ตลอดเวลา",
        "tier_1_feature_1": "ปลดล็อกตัวล็อกหลู่ปาน 3 มิติ และผังโต๊ะเยี่ยนจี 2 มิติระดับปรมาจารย์ทั้งหมด",
        "tier_1_feature_2": "เสียงบำบัดแบบตะวันออกสำหรับยามเช้าและก่อนนอน",
        "tier_1_feature_3": "รายงานวิเคราะห์ความลื่นไหลในการสัมผัสและสมาธิ",
        "tier_2_title": "แผนกระแสจิตรายปี (แนะนำ)",
        "tier_2_badge": "ทดลองใช้ฟรี · อิงตามข้อเสนอ App Store",
        "tier_2_feature_1": "เข้าถึงบันทึกประวัติศาสตร์ 5,000 ปีและกลไกชั้นยอดทั้งหมด",
        "tier_2_feature_2": "ปลดล็อกเวิร์กช็อป AI บนอุปกรณ์สร้างกลไกและกระดานแบบไร้ขีดจำกัด",
        "tier_2_feature_3": "ระบบติดตามสายตา TrueDepth ขั้นสูงและรายงานสมาธิ HRV ผ่าน Apple Watch",
        "tier_2_feature_4": "ปล่อยโคมลอยอธิษฐานได้ไม่จำกัดและปริศนาโคมไฟ 10 ภาษา",
        "tier_3_title": "บัตรนักสะสมตลอดชีพ",
        "tier_3_badge": "รับตราประทับหยกเหอเถียน · ปลดล็อกถาวร",
        "tier_3_feature_1": "ชำระครั้งเดียวเพื่อเป็นเจ้าของทุกบทเรียนและการอัปเดตในอนาคตตลอดไป",
        "tier_3_feature_2": "สิทธิพิเศษในการประทับตราหยกเหอเถียนสำหรับนักสะสมตลอดชีพ",
        "tier_3_feature_3": "รวมแพ็กเกจขยายกลไกเชิงพื้นที่สำหรับ Apple Vision Pro ในอนาคต",
        "tier_3_feature_4": "ไม่มีความกดดันจากค่าบริการรายเดือน สะสมพิพิธภัณฑ์ศิลปะโบราณดิจิทัลอันเงียบสงบ",
        "eula_disclosure_title": "เงื่อนไขการต่ออายุการสมัครสมาชิกอัตโนมัติของ App Store",
        "eula_disclosure_text": "การชำระเงินจะถูกเรียกเก็บจากบัญชี Apple ID ของคุณเมื่อยืนยันการสั่งซื้อ การสมัครสมาชิกจะต่ออายุโดยอัตโนมัติเว้นแต่จะยกเลิกอย่างน้อย 24 ชั่วโมงก่อนสิ้นสุดระยะเวลาปัจจุบัน บัญชีของคุณจะถูกเรียกเก็บเงินสำหรับการต่ออายุภายใน 24 ชั่วโมงก่อนสิ้นสุดระยะเวลาปัจจุบัน คุณสามารถจัดการและยกเลิกการสมัครของคุณในการตั้งค่าบัญชี App Store ได้ตลอดเวลาหลังจากซื้อ",
        "footer_rights": "สงวนลิขสิทธิ์ © 2026 ทีมงาน MindCraft Zen สงวนลิขสิทธิ์ทั้งหมด",
        "footer_privacy": "นโยบายความเป็นส่วนตัว",
        "footer_eula": "ข้อตกลงใบอนุญาตมาตรฐานของ Apple (Standard EULA)",
        "footer_support": "ฝ่ายสนับสนุนและติดต่อ: howly7777777@gmail.com",
    }
}

PRIVACY_DATA = {
    "zh-Hant": {
        "page_title": "隱私權政策 · 心象天工 MindCraft Zen",
        "back_to_home": "← 返回首頁",
        "last_updated": "最後更新日期：2026 年 10 月 19 日",
        "title": "心象天工 (MindCraft Zen) 隱私權保護政策",
        "summary": "我們堅信，隱私是一項基本人權。在《心象天工》中，我們將「極致隱私」融入應用的每一行代碼。本應用遵循 100% 端側運算架構，絕不收集、追蹤、儲存或向任何第三方伺服器傳輸您的個人識別資訊、遊戲進度或生物特徵數據。",
        "sec_1_title": "1. 100% 端側神經網路與數據本地化",
        "sec_1_body": "《心象天工》的所有 3D 空間解算、AI 殘局演算法生成、物理模擬與圖像渲染，均 100% 於您手持的 Apple 設備（A 系列 / M 系列晶片之 Neural Engine）本地即時運算。應用程式不依賴外部伺服器連線，離線狀態下亦可完整暢玩所有功能。您的遊戲存檔與歷史成就僅保存在設備沙盒或您個人專屬的私人 iCloud 容器中，我們無法也不會讀取任何內容。",
        "sec_2_title": "2. TrueDepth 原深感測相機與視線專注追蹤",
        "sec_2_body": "若您在應用中主動啟用「視線專注引導」功能，應用將透過 Apple TrueDepth 前置鏡頭與 Vision Framework 即時評估您的視線凝神程度，藉此動態微調背景光影與環境白噪音。\n\n我們在此鄭重聲明：\n• 視線計算為即時、短暫的端側記憶體矩陣運算，絕不錄製、儲存或截取任何照片、影片或面部幾何網格特徵。\n• 相機數據永遠不會離開您的本機設備，更絕不傳輸至任何雲端伺服器或第三方機構。\n• 您可隨時在「心智工坊」或 iOS 系統「設定 > 隱私權」中關閉相機存取權限，關閉後不影響其他遊戲核心玩法。",
        "sec_3_title": "3. Apple HealthKit 與心率變異度 (HRV) 數據",
        "sec_3_body": "若您配戴 Apple Watch 並在應用中主動授權 HealthKit 存取權限，《心象天工》僅讀取您的「心率變異度」(Heart Rate Variability, HRV) 樣本，用於在解題前後為您呈現自律神經放鬆與專注心流指數。\n\n依據 Apple 審核規範與 HealthKit 嚴格保護標準：\n• 健康數據僅於本機記憶體中短暫分析，絕不上傳至任何外部伺服器。\n• 我們嚴格禁止且絕不會將您的 HealthKit 數據出售給廣告商、數據代理商或任何第三方市場行銷機構。\n• 您可隨時在 iOS「健康」應用或系統「設定 > 隱私權 > 健康」中撤銷存取授權。",
        "sec_4_title": "4. Apple StoreKit 2 交易與訂閱安全",
        "sec_4_body": "《心象天工》的應用內購買 (In-App Purchase) 與會員訂閱完全由 Apple 官方 StoreKit 2 框架直接處理。所有交易均透過您的 Apple ID 完成，採用 Apple 的銀行級加密保護。\n我們無法獲取、存儲或接觸您的信用卡號碼、銀行帳戶、帳單地址或真實身份資訊。所有關於自動續期、方案變更與取消訂閱，均由您在 iOS「設定 > Apple ID > 訂閱項目」中完全自主掌控。",
        "sec_5_title": "5. 零第三方追蹤與零廣告 SDK",
        "sec_5_body": "《心象天工》不包含任何第三方數據分析 SDK（例如 Google Analytics、Firebase Analytics 等），亦不包含任何第三方廣告行銷追蹤插件。我們絕不進行跨應用追蹤 (App Tracking Transparency)，亦不產生或收集 IDFA (廣告識別碼)。",
        "sec_6_title": "6. 兒童隱私保護 (COPPA & GDPR-K)",
        "sec_6_body": "《心象天工》是一款適合全年齡層沉浸的益智文化與專注應用。我們嚴格遵守美國《兒童在線隱私保護法》(COPPA) 及歐盟《通用數據保護條例》(GDPR)。我們不會刻意收集未成年人的任何個人資訊。若家長發現任何疑問，請隨時聯絡我們，我們將第一時間全力協助。",
        "sec_7_title": "7. 數據刪除與完全控制權",
        "sec_7_body": "您對自己的數據擁有 100% 的最高控制權。若您需要徹底刪除所有本機進度，只需在應用內的「設定」中點擊「重置所有進度」，或直接從您的 iOS 設備中解除安裝應用程式，所有本地沙盒數據即刻永久清除。",
        "sec_8_title": "8. 條款協議與聯絡支援",
        "sec_8_body": "本應用的使用同時遵循 Apple 官方標準最終用戶許可協議 (Standard EULA)。\n\n如果您對本隱私權政策有任何疑問、建議或需要技術支援，歡迎隨時透過電子郵件與我們的獨立開發團隊聯繫：\n官方電子郵件：howly7777777@gmail.com\n官方專案網址：https://howly7777777-svg.github.io/mindcraft",
    },
    "zh-Hans": {
        "page_title": "隐私政策 · 心象天工 MindCraft Zen",
        "back_to_home": "← 返回首页",
        "last_updated": "最后更新日期：2026 年 10 月 19 日",
        "title": "心象天工 (MindCraft Zen) 隐私保护政策",
        "summary": "我们坚信，隐私是一项基本人权。在《心象天工》中，我们将“极致隐私”融入应用的每一行代码。本应用遵循 100% 端侧运算架构，绝不收集、追踪、储存或向任何第三方服务器传输您的个人识别信息、游戏进度或生物特征数据。",
        "sec_1_title": "1. 100% 端侧神经网络与数据本地化",
        "sec_1_body": "《心象天工》的所有 3D 空间解算、AI 残局算法生成、物理模拟与图像渲染，均 100% 于您手持的 Apple 设备（A 系列 / M 系列芯片之 Neural Engine）本地即时运算。应用程序不依赖外部服务器连线，离线状态下亦可完整畅玩所有功能。您的游戏存档与历史成就仅保存在设备沙盒或您个人专属的私人 iCloud 容器中，我们无法也不会读取任何内容。",
        "sec_2_title": "2. TrueDepth 原深感测相机与视线专注追踪",
        "sec_2_body": "若您在应用中主动启用“视线专注引导”功能，应用将透过 Apple TrueDepth 前置镜头与 Vision Framework 即时评估您的视线凝神程度，藉此动态微调背景光影与环境白噪音。\n\n我们在此郑重声明：\n• 视线计算为即时、短暂的端侧记忆体矩阵运算，绝不录制、储存或截取任何照片、视频或面部几何网格特征。\n• 相机数据永远不会离开您的本机设备，更绝不传输至任何云端服务器或第三方机构。\n• 您可随时在“心智工坊”或 iOS 系统“设置 > 隐私”中关闭相机访问权限，关闭后不影响其他游戏核心玩法。",
        "sec_3_title": "3. Apple HealthKit 与心率变异度 (HRV) 数据",
        "sec_3_body": "若您配戴 Apple Watch 并在应用中主动授权 HealthKit 访问权限，《心象天工》仅读取您的“心率变异度”(Heart Rate Variability, HRV) 样本，用于在解题前后为您呈现自律神经放松与专注心流指数。\n\n依据 Apple 审核规范与 HealthKit 严格保护标准：\n• 健康数据仅于本机内存中短暂分析，绝不上传至任何外部服务器。\n• 我们严格禁止且绝不会将您的 HealthKit 数据出售给广告商、数据代理商或任何第三方市场行销机构。\n• 您可随时在 iOS“健康”应用或系统“设置 > 隐私 > 健康”中撤销访问授权。",
        "sec_4_title": "4. Apple StoreKit 2 交易与订阅安全",
        "sec_4_body": "《心象天工》的应用内购买 (In-App Purchase) 与会员订阅完全由 Apple 官方 StoreKit 2 框架直接处理。所有交易均透过您的 Apple ID 完成，采用 Apple 的银行级加密保护。\n我们无法获取、存储或接触您的信用卡号码、银行账户、账单地址或真实身份信息。所有关于自动续期、方案变更与取消订阅，均由您在 iOS“设置 > Apple ID > 订阅项目”中完全自主掌控。",
        "sec_5_title": "5. 零第三方追踪与零广告 SDK",
        "sec_5_body": "《心象天工》不包含任何第三方数据分析 SDK（例如 Google Analytics、Firebase Analytics 等），亦不包含任何第三方广告行销追踪插件。我们绝不进行跨应用追踪 (App Tracking Transparency)，亦不产生或收集 IDFA (广告识别码)。",
        "sec_6_title": "6. 儿童隐私保护 (COPPA & GDPR-K)",
        "sec_6_body": "《心象天工》是一款适合全年龄段沉浸的益智文化与专注应用。我们严格遵守美国《儿童在线隐私保护法》(COPPA) 及欧盟《通用数据保护条例》(GDPR)。我们不会刻意收集未成年人的任何个人信息。若家长发现任何疑问，请随时联络我们，我们将第一时间全力协助。",
        "sec_7_title": "7. 数据删除与完全控制权",
        "sec_7_body": "您对自己的数据拥有 100% 的最高控制权。若您需要彻底删除所有本机进度，只需在应用内的“设置”中点击“重置所有进度”，或直接从您的 iOS 设备中卸载应用程序，所有本地沙盒数据即刻永久清除。",
        "sec_8_title": "8. 条款协议与联络支援",
        "sec_8_body": "本应用的使用同时遵循 Apple 官方标准最终用户许可协议 (Standard EULA)。\n\n如果您对本隐私政策有任何疑问、建议或需要技术支援，欢迎随时通过电子邮件与我们的独立开发团队联系：\n官方电子邮件：howly7777777@gmail.com\n官方项目网址：https://howly7777777-svg.github.io/mindcraft",
    },
    "en": {
        "page_title": "Privacy Policy · MindCraft Zen",
        "back_to_home": "← Back to Home",
        "last_updated": "Last Updated: October 19, 2026",
        "title": "MindCraft Zen Privacy Policy",
        "summary": "We believe that privacy is a fundamental human right. In MindCraft Zen, privacy-by-design is embedded into every line of code. Our app adopts a 100% on-device architecture: we never collect, track, store, or transmit your personal identity, puzzle progress, or biometric data to any external server.",
        "sec_1_title": "1. 100% On-Device Neural Engine & Local Processing",
        "sec_1_body": "All 3D spatial calculations, on-device AI endgame synthesis, physics simulations, and visual rendering run entirely on your Apple device's Neural Engine and GPU. MindCraft Zen functions completely offline with zero reliance on cloud servers. Your game saves and unlocked achievements reside exclusively within your local application sandbox or your private Apple iCloud container.",
        "sec_2_title": "2. TrueDepth Camera & Gaze Focus Guidance",
        "sec_2_body": "If you explicitly enable 'Gaze Focus Guidance', MindCraft Zen uses Apple's front-facing TrueDepth camera and Vision Framework locally to gauge gaze stability and gently adjust ambient temple lighting and wood white noise.\n\nWe strictly guarantee:\n• Gaze calculations are transient matrix operations in local memory. We never record, photograph, save, or capture any photos, video feeds, or facial geometries.\n• Camera data never leaves your device and is never uploaded to any remote server or third-party entity.\n• You can revoke camera permission at any time in iOS Settings > Privacy & Security > Camera.",
        "sec_3_title": "3. Apple HealthKit & Heart Rate Variability (HRV)",
        "sec_3_body": "If you wear an Apple Watch and grant HealthKit read permission, MindCraft Zen accesses only your Heart Rate Variability (HRV) metrics to illustrate your autonomic nervous system calming and mindful flow state before and after sessions.\n\nUnder strict Apple HealthKit review standards:\n• Health data is analyzed strictly in local memory and is never transmitted to any external server.\n• We strictly prohibit and never sell or share your HealthKit data with advertisers, data brokers, or third-party marketing platforms.\n• You can revoke HealthKit permission at any time in iOS Settings > Privacy & Security > Health.",
        "sec_4_title": "4. Apple StoreKit 2 Transactions & Subscriptions",
        "sec_4_body": "All in-app purchases and auto-renewing subscriptions are processed directly and securely by Apple StoreKit 2 via your Apple ID. We never have access to, nor do we store, your credit card numbers, billing addresses, or real-world identities. All subscription management, renewals, and cancellations are fully controlled by you in your Apple ID account settings.",
        "sec_5_title": "5. Zero Third-Party Analytics & Zero Ad SDKs",
        "sec_5_body": "MindCraft Zen contains zero third-party analytics trackers (such as Google Analytics or Firebase Analytics) and zero advertising SDKs. We do not engage in cross-app tracking (App Tracking Transparency) and do not collect IDFA advertising identifiers.",
        "sec_6_title": "6. Children's Online Privacy Protection (COPPA & GDPR-K)",
        "sec_6_body": "MindCraft Zen is designed for users of all ages. We strictly comply with the Children's Online Privacy Protection Act (COPPA) and EU GDPR regulations. We do not knowingly solicit or collect any personal information from minors.",
        "sec_7_title": "7. Data Deletion & Complete User Control",
        "sec_7_body": "You retain absolute ownership of your data. You can erase all local progress at any time by selecting 'Reset All Progress' in the in-app settings, or simply by deleting the app from your device, which instantly purges all sandbox data.",
        "sec_8_title": "8. Terms of Use & Support Contact",
        "sec_8_body": "Your use of MindCraft Zen is also governed by Apple's Standard End User License Agreement (Standard EULA).\n\nIf you have any questions or feedback regarding this policy, please contact our team at:\nSupport Email: howly7777777@gmail.com\nWebsite: https://howly7777777-svg.github.io/mindcraft",
    },
    "ja": {
        "page_title": "プライバシーポリシー · 心象天工 MindCraft Zen",
        "back_to_home": "← ホームに戻る",
        "last_updated": "最終更新日：2026年10月19日",
        "title": "心象天工 (MindCraft Zen) プライバシーポリシー",
        "summary": "私たちは、プライバシーは基本的人権であると信じています。『心象天工』では、100%オンデバイス処理アーキテクチャを採用しており、お客様の個人識別情報、ゲームの進行状況、生体認証データを外部サーバーに収集・追跡・保存することは一切ありません。",
        "sec_1_title": "1. 100% オンデバイス Neural Engine と完全ローカル処理",
        "sec_1_body": "『心象天工』におけるすべての3D空間計算、AIパズル生成、物理演算は、お客様がお持ちのAppleデバイス上のNeural EngineおよびGPUで完結します。外部サーバーへの通信は一切不要で、完全オフラインで安心してお楽しみいただけます。セーブデータはお使いの端末のサンドボックスまたはお客様のプライベートなiCloudにのみ安全に保管されます。",
        "sec_2_title": "2. TrueDepth カメラと視線集中ガイダンス",
        "sec_2_body": "「視線集中ガイダンス」機能を有効にした場合、TrueDepth 前面カメラを用いてローカルで視線の安定度を測定し、照明や環境音を調和させます。\n\n• 視線計算は一時的なメモリ演算のみで行われ、写真、動画、顔の幾何学的データを記録・保存することは決してありません。\n• カメラデータがお使いのデバイスから外部に送信されることは絶対にありません。\n• iOSの「設定 > プライバシーとセキュリティ > カメラ」からいつでもアクセス権を取り消すことができます。",
        "sec_3_title": "3. Apple HealthKit と心拍変動 (HRV) データ",
        "sec_3_body": "Apple Watch をご使用中にお客様が許可された場合、『心象天工』は心拍変動 (HRV) のみをローカルで読み取り、パズル前後の自律神経リラックス度を可視化します。\n\n• ヘルスケアデータは端末内メモリでのみ一時的に分析され、外部サーバーに送信されることはありません。\n• HealthKit データを広告主や第三者に販売・提供することは固く禁じられており、一切行いません。\n• iOSの「設定 > プライバシーとセキュリティ > ヘルスケア」からいつでも許可を取り消せます。",
        "sec_4_title": "4. Apple StoreKit 2 による安全な決済とサブスクリプション",
        "sec_4_body": "すべてのアプリ内課金およびサブスクリプションは、Apple公式の StoreKit 2 フレームワークを通じて安全に処理されます。クレジットカード番号や請求先情報が当方に渡ることはありません。更新や解約は、Apple ID のアカウント設定からいつでもお客様ご自身で管理いただけます。",
        "sec_5_title": "5. サードパーティ製トラッカーおよび広告SDKの排除",
        "sec_5_body": "『心象天工』には、Google Analytics や Firebase Analytics などの分析トラッカーや、広告SDKは一切含まれていません。アプリ間トラッキングや広告識別子 (IDFA) の収集も一切行いません。",
        "sec_6_title": "6. お子様のプライバシー保護 (COPPA & GDPR-K)",
        "sec_6_body": "すべての年齢層に安心してご利用いただけるよう設計されています。未成年者から個人情報を意図的に収集することは一切ありません。",
        "sec_7_title": "7. データ削除と完全な制御権",
        "sec_7_body": "アプリ内の設定から「すべての進捗をリセット」するか、アプリを削除することで、端末内のすべてのデータをいつでも完全に消去できます。",
        "sec_8_title": "8. 利用規約およびお問い合わせ",
        "sec_8_body": "本アプリの利用には、Apple公式の標準使用許諾契約 (Standard EULA) が適用されます。\n\nお問い合わせ窓口：\nメール：howly7777777@gmail.com\n公式ウェブサイト：https://howly7777777-svg.github.io/mindcraft",
    },
    "ko": {
        "page_title": "개인정보 처리방침 · 심상천공 MindCraft Zen",
        "back_to_home": "← 홈으로 돌아가기",
        "last_updated": "최종 수정일: 2026년 10월 19일",
        "title": "심상천공 (MindCraft Zen) 개인정보 처리방침",
        "summary": "우리는 개인정보 보호가 기본적인 인권이라고 굳게 믿습니다. '심상천공'은 100% 온디바이스 아키텍처를 채택하여 어떠한 개인 식별 정보, 게임 진행 데이터, 생체 정보를 외부 서버로 수집, 추적, 저장, 전송하지 않습니다.",
        "sec_1_title": "1. 100% 온디바이스 Neural Engine 및 데이터 로컬 처리",
        "sec_1_body": "모든 3D 공간 연산, AI 퍼즐 생성, 물리 시뮬레이션은 기기 내부의 Apple Neural Engine 칩에서 독립적으로 실행됩니다. 외부 클라우드 통신에 의존하지 않으며 완벽한 오프라인 플레이가 가능합니다. 저장 데이터는 기기 로컬 샌드박스 또는 사용자의 개인 iCloud 컨테이너에만 안전하게 보관됩니다.",
        "sec_2_title": "2. TrueDepth 카메라 및 시선 집중 추적 안내",
        "sec_2_body": "사용자가 '시선 집중 안내' 기능을 활성화한 경우, 전면 TrueDepth 카메라를 통해 시선 안정성을 로컬에서 분석하여 조명과 명상 사운드를 조화롭게 조절합니다.\n\n• 시선 계산은 기기 메모리 내에서 일시적으로만 수행되며 사진, 동영상, 안면 기하 데이터를 일체 저장하거나 녹화하지 않습니다.\n• 카메라 데이터는 기기 외부로 절대 전송되지 않습니다.\n• iOS '설정 > 개인정보 보호 및 보안 > 카메라'에서 언제든 권한을 취소할 수 있습니다.",
        "sec_3_title": "3. Apple HealthKit 및 심박변이도 (HRV) 데이터",
        "sec_3_body": "사용자의 허가를 받은 경우에 한해 심박변이도(HRV) 데이터를 로컬에서 읽어 퍼즐 풀이 전후 자율신경 이완 지수를 분석합니다.\n\n• 건강 데이터는 기기 메모리에서만 일시적으로 분석되며 외부 서버로 전송되지 않습니다.\n• HealthKit 데이터를 광고주나 제3자에게 판매하거나 제공하지 않습니다.\n• iOS '설정 > 개인정보 보호 및 보안 > 건강'에서 언제든 권한을 철회할 수 있습니다.",
        "sec_4_title": "4. Apple StoreKit 2 결제 및 구독 보안",
        "sec_4_body": "모든 인앱 구매 및 구독 결제는 Apple StoreKit 2를 통해 직접 처리됩니다. 개발자는 신용카드 정보나 결제 주소에 일체 접근할 수 없으며, 모든 구독 관리는 Apple ID 계정 설정에서 직접 관리하실 수 있습니다.",
        "sec_5_title": "5. 제3자 분석기 및 광고 SDK 배제",
        "sec_5_body": "구글 애널리틱스 등 제3자 추적 SDK나 광고 SDK를 일체 포함하지 않으며, 앱 간 추적이나 광고 식별자(IDFA)를 수집하지 않습니다.",
        "sec_6_title": "6. 어린이 개인정보 보호 (COPPA 준수)",
        "sec_6_body": "모든 연령층이 안심하고 이용할 수 있는 앱으로서, 미성년자의 개인정보를 의도적으로 수집하지 않습니다.",
        "sec_7_title": "7. 데이터 삭제 및 통제권",
        "sec_7_body": "앱 설정 내 '모든 진행 상황 초기화'를 누르거나 앱을 삭제하시면 모든 로컬 데이터가 즉시 영구 삭제됩니다.",
        "sec_8_title": "8. 이용약관 및 고객지원 문의",
        "sec_8_body": "본 앱의 이용은 Apple 표준 최종 사용자 사용권 계약(Standard EULA)을 따릅니다.\n\n고객지원 이메일: howly7777777@gmail.com\n웹사이트: https://howly7777777-svg.github.io/mindcraft",
    },
    "de": {
        "page_title": "Datenschutzerklärung · MindCraft Zen",
        "back_to_home": "← Zurück zur Startseite",
        "last_updated": "Zuletzt aktualisiert: 19. Oktober 2026",
        "title": "MindCraft Zen Datenschutzerklärung",
        "summary": "Wir sind überzeugt, dass Privatsphäre ein grundlegendes Menschenrecht ist. MindCraft Zen basiert auf einer 100%igen On-Device-Architektur: Wir erfassen, verfolgen, speichern oder übertragen niemals personenbezogene Daten, Spielfortschritte oder biometrische Daten an externe Server.",
        "sec_1_title": "1. 100% On-Device Neural Engine & Lokale Datenverarbeitung",
        "sec_1_body": "Alle 3D-Berechnungen, KI-Puzzle-Generierungen und Physiksimulationen laufen vollständig auf der Neural Engine Ihres Apple-Geräts ab. Die App funktioniert vollkommen offline. Ihre Speicherdaten verbleiben ausschließlich in der lokalen App-Sandbox oder Ihrem privaten iCloud-Container.",
        "sec_2_title": "2. TrueDepth-Kamera & Blickfokus-Führung",
        "sec_2_body": "Wenn Sie die 'Blickfokus-Führung' aktivieren, analysiert die TrueDepth-Frontkamera lokal die Blickstabilität, um Beleuchtung und Klang optimal anzupassen.\n\n• Berechnungen erfolgen rein flüchtig im Gerätespeicher; es werden keine Fotos, Videos oder Gesichtsgeometrien gespeichert.\n• Die Kameradaten verlassen niemals Ihr Gerät.\n• Sie können die Berechtigung jederzeit in den iOS-Einstellungen unter 'Datenschutz & Sicherheit > Kamera' widerrufen.",
        "sec_3_title": "3. Apple HealthKit & Herzfrequenzvariabilität (HRV)",
        "sec_3_body": "Mit Ihrer ausdrücklichen Genehmigung liest die App ausschließlich Ihre Herzfrequenzvariabilität (HRV) über HealthKit lokal aus, um Entspannungszustände vor und nach dem Lösen darzustellen.\n\n• Gesundheitsdaten werden niemals an externe Server übertragen.\n• Eine Weitergabe oder ein Verkauf von HealthKit-Daten an Werbetreibende ist strengstens ausgeschlossen.\n• Sie können den Zugriff jederzeit in den iOS-Einstellungen widerrufen.",
        "sec_4_title": "4. Apple StoreKit 2 Abonnements & Zahlungssicherheit",
        "sec_4_body": "In-App-Käufe und Abonnements werden direkt und sicher von Apple über StoreKit 2 abgewickelt. Wir haben zu keinem Zeitpunkt Zugriff auf Ihre Zahlungsdaten. Die Verwaltung und Kündigung erfolgt bequem über Ihre Apple-ID-Einstellungen.",
        "sec_5_title": "5. Keine Drittanbieter-Tracker oder Werbe-SDKs",
        "sec_5_body": "MindCraft Zen enthält keinerlei Analyse-Tracker von Drittanbietern und keine Werbe-SDKs. Es findet kein App-übergreifendes Tracking statt.",
        "sec_6_title": "6. Schutz der Privatsphäre von Kindern (COPPA & DSGVO)",
        "sec_6_body": "Unsere App richtet sich an alle Altersgruppen und sammelt wissentlich keinerlei Daten von Minderjährigen.",
        "sec_7_title": "7. Datenlöschung & Vollständige Kontrolle",
        "sec_7_body": "Sie können alle lokalen Daten jederzeit in den App-Einstellungen über 'Fortschritt zurücksetzen' oder durch Deinstallation der App restlos löschen.",
        "sec_8_title": "8. Nutzungsbedingungen & Support-Kontakt",
        "sec_8_body": "Die Nutzung unterliegt der Apple Standard-EULA.\n\nSupport-Kontakt: howly7777777@gmail.com\nWebsite: https://howly7777777-svg.github.io/mindcraft",
    },
    "fr": {
        "page_title": "Politique de Confidentialité · MindCraft Zen",
        "back_to_home": "← Retour à l'accueil",
        "last_updated": "Dernière mise à jour : 19 octobre 2026",
        "title": "Politique de Confidentialité de MindCraft Zen",
        "summary": "Nous croyons que la vie privée est un droit fondamental. MindCraft Zen fonctionne selon une architecture 100% sur l'appareil : nous ne collectons, ne traquons, ne stockons et ne transmettons aucune donnée personnelle ou biométrique à des serveurs tiers.",
        "sec_1_title": "1. Traitement 100% Local & Neural Engine sur l'appareil",
        "sec_1_body": "Tous les calculs géométriques en 3D et la génération de casse-têtes par IA s'exécutent entièrement sur la puce de votre appareil Apple. L'application est totalement utilisable hors ligne. Vos données de sauvegarde sont stockées uniquement dans le bac à sable local de votre appareil ou dans votre compte iCloud privé.",
        "sec_2_title": "2. Caméra TrueDepth & Suivi de Concentration Visuelle",
        "sec_2_body": "Si vous activez le 'Guidage Visuel', la caméra avant TrueDepth évalue localement la stabilité de votre regard pour harmoniser la lumière et les sons d'ambiance.\n\n• Les calculs sont éphémères en mémoire vive locale. Aucune photo, vidéo ou géométrie faciale n'est jamais enregistrée.\n• Les données de la caméra ne quittent jamais votre appareil.\n• Vous pouvez révoquer l'autorisation à tout moment dans Réglages > Confidentialité > Appareil photo.",
        "sec_3_title": "3. Apple HealthKit & Variabilité de la Fréquence Cardiaque (VRC)",
        "sec_3_body": "Avec votre accord explicite, MindCraft Zen lit uniquement les données de Variabilité de la Fréquence Cardiaque (VRC) via HealthKit pour illustrer votre relaxation avant et après chaque session.\n\n• Les données de santé ne sont jamais transmises à aucun serveur externe.\n• Nous ne vendons ni ne partageons jamais vos données de santé avec des tiers.\n• Vous pouvez révoquer l'accès à tout moment dans Réglages > Santé.",
        "sec_4_title": "4. Sécurité des Paiements StoreKit 2 d'Apple",
        "sec_4_body": "Tous les achats intégrés et abonnements sont gérés directement par Apple StoreKit 2 via votre compte Apple ID. Nous n'avons aucun accès à vos coordonnées bancaires. Vous pouvez gérer ou résilier vos abonnements à tout moment dans vos réglages Apple ID.",
        "sec_5_title": "5. Zéro Traqueur Tiers & Zéro SDK Publicitaire",
        "sec_5_body": "MindCraft Zen ne contient aucun SDK d'analyse tiers ni aucun module publicitaire. Nous ne pratiquons aucun suivi inter-applications.",
        "sec_6_title": "6. Protection de l'Enfance (COPPA & RGPD-K)",
        "sec_6_body": "Notre application est sûre pour tous les âges et ne collecte aucune donnée auprès des mineurs.",
        "sec_7_title": "7. Suppression des Données & Contrôle Total",
        "sec_7_body": "Vous pouvez réinitialiser toutes les données dans les réglages de l'application ou en supprimant l'application de votre appareil.",
        "sec_8_title": "8. Conditions d'Utilisation & Assistance",
        "sec_8_body": "L'utilisation est soumise au contrat de licence standard Apple (Standard EULA).\n\nContact support : howly7777777@gmail.com\nSite web : https://howly7777777-svg.github.io/mindcraft",
    },
    "es": {
        "page_title": "Política de Privacidad · MindCraft Zen",
        "back_to_home": "← Volver al inicio",
        "last_updated": "Última actualización: 19 de octubre de 2026",
        "title": "Política de Privacidad de MindCraft Zen",
        "summary": "Creemos firmemente que la privacidad es un derecho humano fundamental. MindCraft Zen opera con una arquitectura 100% en el dispositivo: nunca recopilamos, rastreamos, almacenamos ni transmitimos tus datos personales, progreso o información biométrica a servidores externos.",
        "sec_1_title": "1. 100% Neural Engine en el Dispositivo y Procesamiento Local",
        "sec_1_body": "Todos los cálculos 3D y la generación de acertijos se ejecutan en el chip de tu dispositivo Apple. La aplicación funciona sin conexión a internet. Tus datos de guardado se mantienen exclusivamente en el almacenamiento local seguro de tu dispositivo o en tu contenedor privado de iCloud.",
        "sec_2_title": "2. Cámara TrueDepth y Seguimiento de Concentración Visual",
        "sec_2_body": "Si activas la 'Guía Visual', la cámara TrueDepth frontal evalúa localmente la estabilidad de tu mirada para calibrar la iluminación y el sonido ambiente.\n\n• Los cálculos son temporales en memoria. No se guardan ni graban fotos, videos ni geometrías faciales.\n• Los datos nunca salen de tu dispositivo.\n• Puedes revocar el permiso en cualquier momento desde Ajustes > Privacidad > Cámara.",
        "sec_3_title": "3. Apple HealthKit y Variabilidad de Frecuencia Cardíaca (VFC)",
        "sec_3_body": "Con tu autorización, la app lee únicamente la Variabilidad de la Frecuencia Cardíaca (VFC) a través de HealthKit para mostrar tu nivel de calma antes y después de resolver los acertijos.\n\n• Los datos de salud jamás se envían a servidores externos.\n• Nunca compartimos ni vendemos tus datos de salud a anunciantes o terceros.\n• Puedes revocar el acceso en cualquier momento desde Ajustes > Privacidad > Salud.",
        "sec_4_title": "4. Seguridad en Pagos y Suscripciones con StoreKit 2",
        "sec_4_body": "Las compras dentro de la app y las suscripciones son procesadas directamente por Apple mediante StoreKit 2 con tu Apple ID. No tenemos acceso a tus datos de pago. Puedes administrar o cancelar tu suscripción desde los ajustes de tu Apple ID.",
        "sec_5_title": "5. Cero Rastreadores de Terceros y Cero SDKs Publicitarios",
        "sec_5_body": "MindCraft Zen no incluye herramientas de análisis de terceros ni SDKs de publicidad. No realizamos seguimiento entre apps ni recopilamos el identificador IDFA.",
        "sec_6_title": "6. Protección de la Privacidad Infantil (COPPA)",
        "sec_6_body": "Nuestra aplicación es apta para todas las edades y no recopila deliberadamente información de menores.",
        "sec_7_title": "7. Eliminación de Datos y Control Absoluto",
        "sec_7_body": "Puedes restablecer tu progreso en los ajustes de la aplicación o desinstalar la app para borrar todos los datos locales al instante.",
        "sec_8_title": "8. Términos de Uso y Soporte",
        "sec_8_body": "El uso de la app se rige por el Contrato de Licencia Estándar de Apple (Standard EULA).\n\nContacto de soporte: howly7777777@gmail.com\nSitio web: https://howly7777777-svg.github.io/mindcraft",
    },
    "vi": {
        "page_title": "Chính Sách Quyền Riêng Tư · MindCraft Zen",
        "back_to_home": "← Quay lại trang chủ",
        "last_updated": "Cập nhật lần cuối: 19 tháng 10 năm 2026",
        "title": "Chính Sách Quyền Riêng Tư Của Tâm Tượng Thiên Công (MindCraft Zen)",
        "summary": "Chúng tôi tin rằng quyền riêng tư là quyền cơ bản của con người. Tâm Tượng Thiên Công vận hành trên cấu trúc 100% cục bộ trên thiết bị: chúng tôi không bao giờ thu thập, theo dõi, lưu trữ hay chuyển tiếp bất kỳ thông tin cá nhân, tiến trình chơi hay dữ liệu sinh trắc học nào lên máy chủ bên ngoài.",
        "sec_1_title": "1. 100% Neural Engine Cục Bộ & Xử Lý Dữ Liệu Nội Bộ",
        "sec_1_body": "Mọi thuật toán tính toán không gian 3D và tạo câu đố AI đều chạy trực tiếp trên chip thiết bị Apple của bạn. Ứng dụng hoạt động hoàn hảo khi ngoại tuyến. Dữ liệu lưu trữ chỉ nằm an toàn trong vùng bảo mật của thiết bị hoặc tài khoản iCloud riêng tư của bạn.",
        "sec_2_title": "2. Camera TrueDepth & Dẫn Lối Tập Trung Ánh Nhìn",
        "sec_2_body": "Nếu bạn bật tính năng 'Dẫn Lối Tập Trung Ánh Nhìn', camera TrueDepth phía trước sẽ đánh giá độ ổn định của ánh nhìn trong bộ nhớ tạm để điều chỉnh ánh sáng và âm thanh phù hợp.\n\n• Tính toán hoàn toàn diễn ra trong bộ nhớ tạm; tuyệt đối không chụp ảnh, quay video hay lưu lưới hình học khuôn mặt.\n• Dữ liệu camera không bao giờ rời khỏi thiết bị của bạn.\n• Bạn có thể thu hồi quyền trong Cài đặt > Quyền riêng tư > Camera bất kỳ lúc nào.",
        "sec_3_title": "3. Apple HealthKit & Độ Biến Thiên Nhịp Tim (HRV)",
        "sec_3_body": "Khi bạn cho phép, ứng dụng chỉ đọc dữ liệu HRV qua HealthKit để phân tích độ thư giãn và tập trung trước và sau khi giải đố.\n\n• Dữ liệu sức khỏe tuyệt đối không bao giờ tải lên bất kỳ máy chủ nào.\n• Tuyệt đối không chia sẻ hoặc bán dữ liệu HealthKit cho bên thứ ba hoặc nhà quảng cáo.\n• Bạn có thể thu hồi quyền trong Cài đặt > Sức khỏe bất cứ lúc nào.",
        "sec_4_title": "4. Bảo Mật Thanh Toán & Đăng Ký Gói StoreKit 2 Của Apple",
        "sec_4_body": "Các giao dịch mua gói và gia hạn đăng ký được xử lý bảo mật trực tiếp bởi Apple thông qua Apple ID của bạn. Chúng tôi không thể truy cập thông tin thẻ tín dụng của bạn. Bạn toàn quyền quản lý hoặc hủy gói trong Cài đặt Apple ID của mình.",
        "sec_5_title": "5. Không Theo Dõi Bên Thứ Ba & Không SDK Quảng Cáo",
        "sec_5_body": "Tâm Tượng Thiên Công không chứa bất kỳ SDK phân tích dữ liệu bên thứ ba hay SDK quảng cáo nào. Chúng tôi không theo dõi chéo giữa các ứng dụng.",
        "sec_6_title": "6. Bảo Vệ Trẻ Em (Tuân Thủ COPPA)",
        "sec_6_body": "Ứng dụng phù hợp cho mọi lứa tuổi và không cố ý thu thập bất kỳ thông tin nào từ trẻ vị thành niên.",
        "sec_7_title": "7. Xóa Dữ Liệu & Quyền Kiểm Soát Tuyệt Đối",
        "sec_7_body": "Bạn có thể thiết lập lại toàn bộ tiến trình trong phần cài đặt của ứng dụng hoặc gỡ bỏ ứng dụng để xóa vĩnh viễn toàn bộ dữ liệu nội bộ.",
        "sec_8_title": "8. Điều Khoản & Hỗ Trợ",
        "sec_8_body": "Việc sử dụng tuân theo Thỏa thuận Cấp phép Tiêu chuẩn của Apple (Standard EULA).\n\nLiên hệ hỗ trợ: howly7777777@gmail.com\nTrang web: https://howly7777777-svg.github.io/mindcraft",
    },
    "th": {
        "page_title": "นโยบายความเป็นส่วนตัว · MindCraft Zen",
        "back_to_home": "← กลับสู่หน้าหลัก",
        "last_updated": "ปรับปรุงล่าสุด: 19 ตุลาคม 2026",
        "title": "นโยบายความเป็นส่วนตัวของ MindCraft Zen",
        "summary": "เราเชื่อมั่นว่าความเป็นส่วนตัวเป็นสิทธิมนุษยชนขั้นพื้นฐาน MindCraft Zen ทำงานบนสถาปัตยกรรมที่ประมวลผลบนอุปกรณ์ 100% เราไม่เก็บรวบรวม ไม่ติดตาม ไม่จัดเก็บ และไม่ส่งข้อมูลส่วนบุคคล ความคืบหน้าในการเล่น หรือข้อมูลชีวมิติใดๆ ไปยังเซิร์ฟเวอร์ภายนอก",
        "sec_1_title": "1. การประมวลผลบนอุปกรณ์ 100% ด้วย Neural Engine",
        "sec_1_body": "การคำนวณ 3 มิติและการสร้างปริศนาทั้งหมดทำงานบนชิปของอุปกรณ์ Apple ของคุณโดยตรง แอปสามารถเล่นแบบออฟไลน์ได้อย่างสมบูรณ์ ข้อมูลความคืบหน้าของคุณจะถูกจัดเก็บไว้เฉพาะในแซนด์บ็อกซ์ของอุปกรณ์หรือในบัญชี iCloud ส่วนตัวของคุณเท่านั้น",
        "sec_2_title": "2. กล้อง TrueDepth และระบบนำทางสมาธิด้วยสายตา",
        "sec_2_body": "หากคุณเปิดใช้งาน 'ระบบนำทางสมาธิด้วยสายตา' กล้องหน้า TrueDepth จะประเมินความนิ่งของสายตาในหน่วยความจำชั่วคราวเพื่อปรับแสงและเสียงให้เหมาะสม\n\n• การคำนวณทั้งหมดเกิดขึ้นในหน่วยความจำชั่วคราว ไม่มีการบันทึกภาพ วิดีโอ หรือโครงสร้างใบหน้าใดๆ ทั้งสิ้น\n• ข้อมูลกล้องจะไม่ถูกส่งออกจากอุปกรณ์ของคุณโดยเด็ดขาด\n• คุณสามารถเพิกถอนสิทธิ์ได้ตลอดเวลาในการตั้งค่า > ความเป็นส่วนตัว > กล้อง",
        "sec_3_title": "3. Apple HealthKit และความแปรปรวนของอัตราการเต้นของหัวใจ (HRV)",
        "sec_3_body": "หากคุณอนุญาต แอปจะอ่านข้อมูล HRV ผ่าน HealthKit เพื่อวิเคราะห์ระดับความผ่อนคลายและสมาธิก่อนและหลังการแก้ปริศนา\n\n• ข้อมูลสุขภาพจะไม่ถูกส่งไปยังเซิร์ฟเวอร์ภายนอกอย่างเด็ดขาด\n• เราไม่ขายหรือแบ่งปันข้อมูล HealthKit กับบุคคลที่สามหรือผู้โฆษณาโดยเด็ดขาด\n• คุณสามารถเพิกถอนสิทธิ์ได้ตลอดเวลาในการตั้งค่า > สุขภาพ",
        "sec_4_title": "4. ความปลอดภัยในการชำระเงินและสมัครสมาชิกผ่าน StoreKit 2",
        "sec_4_body": "การซื้อภายในแอปและการสมัครสมาชิกทั้งหมดได้รับการจัดการโดยตรงและปลอดภัยผ่าน Apple StoreKit 2 ด้วย Apple ID ของคุณ เราไม่สามารถเข้าถึงข้อมูลบัตรเครดิตของคุณได้ คุณสามารถจัดการหรือยกเลิกการสมัครได้ตลอดเวลาในการตั้งค่า Apple ID ของคุณ",
        "sec_5_title": "5. ปราศจากตัวติดตามบุคคลที่สามและ SDK โฆษณา",
        "sec_5_body": "MindCraft Zen ไม่มี SDK วิเคราะห์ข้อมูลของบุคคลที่สามและไม่มี SDK โฆษณาใดๆ เราไม่มีการติดตามข้ามแอปพลิเคชันอย่างสิ้นเชิง",
        "sec_6_title": "6. การคุ้มครองความเป็นส่วนตัวของเด็ก (COPPA)",
        "sec_6_body": "แอปพลิเคชันของเราปลอดภัยสำหรับทุกช่วงวัย และไม่มีการเก็บรวบรวมข้อมูลส่วนบุคคลจากผู้เยาว์โดยเจตนา",
        "sec_7_title": "7. การลบข้อมูลและการควบคุมอย่างสมบูรณ์",
        "sec_7_body": "คุณสามารถรีเซ็ตความคืบหน้าทั้งหมดได้ในการตั้งค่าของแอป หรือถอนการติดตั้งแอปเพื่อลบข้อมูลทั้งหมดออกจากอุปกรณ์ทันที",
        "sec_8_title": "8. ข้อกำหนดการใช้งานและการติดต่อฝ่ายสนับสนุน",
        "sec_8_body": "การใช้งานอยู่ภายใต้ข้อตกลงใบอนุญาตมาตรฐานของ Apple (Standard EULA)\n\nอีเมลฝ่ายสนับสนุน: howly7777777@gmail.com\nเว็บไซต์: https://howly7777777-svg.github.io/mindcraft",
    }
}

INDEX_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="meta-title">心象天工 · 木構與禪 (MindCraft Zen)</title>
  <meta name="description" id="meta-desc" content="五千年東方古智 · Apple 端側神經網路專注工坊。沈浸於 3D 魯班鎖、2D 宋代燕幾圖、九連環與洛書華容道。">
  <link rel="icon" type="image/png" href="assets/app_icon.png">
  <style>
    :root {
      --bg: #0b0e14;
      --card-bg: rgba(255, 255, 255, 0.04);
      --card-border: rgba(255, 255, 255, 0.09);
      --card-hover: rgba(255, 255, 255, 0.08);
      --gold: #d4af37;
      --gold-light: #f5e6a8;
      --cinnabar: #b8332a;
      --jade: #7aa199;
      --text: #f5f5f7;
      --text-muted: rgba(255, 255, 255, 0.65);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans", "Apple SD Gothic Neo", sans-serif;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }
    a { color: inherit; text-decoration: none; }
    .container { max-width: 1120px; margin: 0 auto; padding: 0 24px; }

    /* Nav */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 14, 20, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--card-border);
    }
    .nav-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 70px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand img {
      width: 42px;
      height: 42px;
      border-radius: 10px;
      box-shadow: 0 4px 12px rgba(212, 175, 55, 0.25);
    }
    .brand-text h1 {
      font-size: 18px;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: #fff;
    }
    .brand-text p {
      font-size: 11px;
      color: var(--gold);
      letter-spacing: 0.5px;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 20px;
    }
    .nav-links a {
      font-size: 14px;
      color: var(--text-muted);
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--gold); }
    .lang-select {
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
      border: 1px solid var(--card-border);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 13px;
      cursor: pointer;
      outline: none;
      transition: all 0.2s;
    }
    .lang-select:hover { border-color: var(--gold); }

    /* Hero */
    .hero {
      padding: 90px 0 70px;
      text-align: center;
      position: relative;
    }
    .hero::before {
      content: "";
      position: absolute;
      top: 10%;
      left: 50%;
      transform: translateX(-50%);
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(212, 175, 55, 0.12) 0%, rgba(11, 14, 20, 0) 70%);
      z-index: -1;
      pointer-events: none;
    }
    .hero-icon {
      width: 108px;
      height: 108px;
      border-radius: 24px;
      box-shadow: 0 16px 40px rgba(212, 175, 55, 0.35);
      margin-bottom: 24px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .hero-badge {
      display: inline-block;
      padding: 6px 16px;
      border-radius: 30px;
      background: rgba(212, 175, 55, 0.1);
      border: 1px solid rgba(212, 175, 55, 0.3);
      color: var(--gold-light);
      font-size: 13px;
      font-weight: 500;
      margin-bottom: 20px;
    }
    .hero-title {
      font-size: clamp(32px, 5vw, 52px);
      font-weight: 800;
      color: #fff;
      margin-bottom: 20px;
      line-height: 1.2;
    }
    .hero-subtitle {
      font-size: clamp(16px, 2vw, 20px);
      color: var(--text-muted);
      max-width: 760px;
      margin: 0 auto 36px;
    }
    .hero-cta-btn {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: linear-gradient(135deg, #d4af37, #b8332a);
      color: #fff;
      font-size: 17px;
      font-weight: 700;
      padding: 16px 36px;
      border-radius: 14px;
      box-shadow: 0 12px 30px rgba(184, 51, 42, 0.35);
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .hero-cta-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 16px 36px rgba(212, 175, 55, 0.45);
    }
    .hero-cta-sub {
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 14px;
    }

    /* Section */
    section { padding: 70px 0; }
    .section-header {
      text-align: center;
      margin-bottom: 50px;
    }
    .section-title {
      font-size: clamp(24px, 3.5vw, 36px);
      font-weight: 700;
      color: #fff;
      margin-bottom: 12px;
    }
    .section-subtitle {
      font-size: 16px;
      color: var(--text-muted);
      max-width: 650px;
      margin: 0 auto;
    }

    /* Grid */
    .grid-2x2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 24px;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 30px;
      transition: all 0.3s;
      position: relative;
      overflow: hidden;
    }
    .card:hover {
      background: var(--card-hover);
      border-color: rgba(212, 175, 55, 0.3);
      transform: translateY(-3px);
    }
    .card-icon {
      font-size: 28px;
      margin-bottom: 16px;
      display: inline-block;
    }
    .card-title {
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 12px;
    }
    .card-desc {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.7;
    }

    /* Tiers */
    .tiers-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 24px;
    }
    .tier-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 22px;
      padding: 34px 28px;
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .tier-card.featured {
      border: 2px solid var(--gold);
      background: rgba(212, 175, 55, 0.05);
    }
    .tier-badge {
      display: inline-block;
      align-self: flex-start;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 16px;
    }
    .tier-badge.monthly { background: rgba(255, 255, 255, 0.12); color: #fff; }
    .tier-badge.annual { background: var(--gold); color: #0b0e14; }
    .tier-badge.lifetime { background: var(--cinnabar); color: #fff; }
    .tier-title {
      font-size: 22px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 16px;
    }
    .tier-features {
      list-style: none;
      margin-top: 10px;
      flex-grow: 1;
    }
    .tier-features li {
      font-size: 14px;
      color: rgba(255, 255, 255, 0.85);
      margin-bottom: 12px;
      display: flex;
      gap: 10px;
      align-items: flex-start;
    }
    .tier-features li::before {
      content: "✦";
      color: var(--gold);
      flex-shrink: 0;
    }

    /* EULA Disclosure Box */
    .disclosure-box {
      margin-top: 50px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 16px;
      padding: 24px 28px;
      text-align: center;
      max-width: 860px;
      margin-left: auto;
      margin-right: auto;
    }
    .disclosure-box h4 {
      font-size: 13px;
      font-weight: 600;
      color: var(--gold);
      margin-bottom: 8px;
      letter-spacing: 0.5px;
    }
    .disclosure-box p {
      font-size: 12px;
      color: rgba(255, 255, 255, 0.55);
      line-height: 1.6;
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--card-border);
      padding: 50px 0 30px;
      margin-top: 60px;
      text-align: center;
    }
    .footer-links {
      display: flex;
      justify-content: center;
      gap: 24px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }
    .footer-links a {
      font-size: 14px;
      color: var(--text-muted);
      transition: color 0.2s;
    }
    .footer-links a:hover { color: var(--gold); }
    .footer-contact {
      font-size: 13px;
      color: var(--gold);
      margin-bottom: 16px;
    }
    .footer-copy {
      font-size: 12px;
      color: rgba(255, 255, 255, 0.4);
    }

    @media (max-width: 768px) {
      .nav-links a:not(.privacy-link) { display: none; }
      .hero { padding: 60px 0 40px; }
    }
  </style>
</head>
<body>
  <!-- Header -->
  <header>
    <div class="container nav-inner">
      <div class="brand">
        <img src="assets/app_icon.png" alt="MindCraft Zen App Icon">
        <div class="brand-text">
          <h1 id="nav-title">心象天工</h1>
          <p id="nav-subtitle">MindCraft Zen</p>
        </div>
      </div>
      <nav class="nav-links">
        <a href="#crafts" id="nav-crafts">四大古智</a>
        <a href="#technology" id="nav-tech">端側禪境</a>
        <a href="#membership" id="nav-tiers">匠人典藏</a>
        <a href="privacy.html" class="privacy-link" id="nav-privacy">隱私政策</a>
        <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" target="_blank" rel="noopener" id="nav-terms">使用條款 (EULA)</a>
        <a href="mailto:howly7777777@gmail.com" id="nav-support" style="color: var(--gold); border: 1px solid rgba(212, 175, 55, 0.4); padding: 5px 12px; border-radius: 16px; font-size: 13px; font-weight: 500;">✉️ 客服支援</a>
        <select class="lang-select" id="lang-select" onchange="changeLanguage(this.value)">
          <option value="zh-Hant">繁體中文</option>
          <option value="zh-Hans">简体中文</option>
          <option value="en">English</option>
          <option value="ja">日本語</option>
          <option value="ko">한국어</option>
          <option value="de">Deutsch</option>
          <option value="fr">Français</option>
          <option value="es">Español</option>
          <option value="vi">Tiếng Việt</option>
          <option value="th">ไทย</option>
        </select>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <img src="assets/app_icon.png" alt="MindCraft Zen App Icon" class="hero-icon">
      <br>
      <div class="hero-badge" id="hero-badge">五千年東方古智 · Apple 端側神經網路專注工坊</div>
      <h2 class="hero-title" id="hero-title">心象天工 · 木構與禪</h2>
      <p class="hero-subtitle" id="hero-subtitle">沈浸於 3D 魯班鎖、2D 宋代燕幾圖、九連環與洛書華容道。在榫卯咬合的清脆回響中，尋回內心的寧靜與專注。</p>
      <a href="https://apps.apple.com" target="_blank" rel="noopener" class="hero-cta-btn">
        <svg width="22" height="22" viewBox="0 0 170 170" fill="currentColor">
          <path d="M150.37 130.25c-2.45 5.66-5.35 10.87-8.71 15.66-4.58 6.53-8.33 11.05-11.22 13.56-4.48 4.12-9.28 6.23-14.42 6.35-3.69 0-8.14-1.05-13.32-3.18-5.19-2.12-9.97-3.17-14.34-3.17-4.58 0-9.49 1.05-14.75 3.17-5.26 2.13-9.5 3.24-12.74 3.35-4.35.13-9.16-1.9-14.42-6.08-3.69-3.04-7.6-7.77-11.74-14.18-6.19-9.5-11.05-20.2-14.58-32.08-3.53-11.89-5.3-23.2-5.3-33.94 0-15.66 4.12-28.53 12.35-38.61 8.23-10.08 18.59-15.22 31.08-15.42 4.13 0 9.07 1.15 14.83 3.44 5.76 2.3 9.4 3.45 10.92 3.45 1.74 0 5.68-1.25 11.83-3.75 6.15-2.5 11.39-3.65 15.72-3.44 14.13.76 25.11 5.98 32.93 15.66-12.39 7.5-18.48 17.72-18.26 30.65.22 10.11 4.13 18.7 11.74 25.76 7.61 7.07 16.74 11.09 27.39 12.07-2.39 7.39-5.11 14.46-8.15 21.22zM119.22 31.85c0-7.72 2.72-14.9 8.15-21.52 5.43-6.63 12.28-10.33 20.54-11.1-1.09 7.94-4.02 15.23-8.8 21.87-4.78 6.63-11.74 10.87-20.87 12.72-.43-.65-.65-1.3-.65-1.97h1.63z"/>
        </svg>
        <span id="hero-cta">前往 App Store 下載</span>
      </a>
      <p class="hero-cta-sub" id="hero-cta-sub">支援 iPhone、iPad 與 Apple Vision Pro</p>
    </div>
  </section>

  <!-- 4 Crafts Section -->
  <section id="crafts">
    <div class="container">
      <div class="section-header">
        <h3 class="section-title" id="crafts-heading">五千年東方智慧 · 四大榫卯與格雷機關</h3>
        <p class="section-subtitle" id="crafts-sub">不著一釘一鉚，純憑空間拓撲、二進位遞歸與奇正相生。</p>
      </div>
      <div class="grid-2x2">
        <div class="card">
          <div class="card-icon">🪵</div>
          <h4 class="card-title" id="craft-1-title">3D 魯班鎖 (孔明鎖)</h4>
          <p class="card-desc" id="craft-1-desc">六子聯方、八角乾坤。三維空間 360 度自由旋轉拆解，感受千斤承重不費一釘一鉚的東方空間拓撲哲學。</p>
        </div>
        <div class="card">
          <div class="card-icon">🪑</div>
          <h4 class="card-title" id="craft-2-title">2D 宋代燕幾圖</h4>
          <p class="card-desc" id="craft-2-desc">南宋黃伯思宴幾之譜，七巧之祖。以案几之離合變幻，演繹宋代文人雅士高雅審美與多維空間組合幾何。</p>
        </div>
        <div class="card">
          <div class="card-icon">💍</div>
          <h4 class="card-title" id="craft-3-title">天道九連環</h4>
          <p class="card-desc" id="craft-3-desc">玉環與雙股金釵交錯。蘊含嚴密二進位格雷碼遞歸天律，一環引一環，解之無窮，修心凝神。</p>
        </div>
        <div class="card">
          <div class="card-icon">⚔️</div>
          <h4 class="card-title" id="craft-4-title">洛書華容道</h4>
          <p class="card-desc" id="craft-4-desc">太極生兩儀，九宮布奇正。曹瞞兵敗華容，方寸棋盤間運籌帷幄，體驗東方古兵法之戰略智慧。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Technology Section -->
  <section id="technology">
    <div class="container">
      <div class="section-header">
        <h3 class="section-title" id="tech-heading">極致純淨 · Apple 前沿科技與禪境心流</h3>
        <p class="section-subtitle" id="tech-sub">為深層心流而生，拒絕浮躁，回歸純粹專注。</p>
      </div>
      <div class="grid-2x2">
        <div class="card">
          <div class="card-icon">🧠</div>
          <h4 class="card-title" id="tech-1-title">100% 端側神經網路</h4>
          <p class="card-desc" id="tech-1-desc">所有 AI 殘局生成與視覺渲染完全於本機晶片執行。零聯網依賴，零伺服器上傳，極致守護個人隱私。</p>
        </div>
        <div class="card">
          <div class="card-icon">👁️</div>
          <h4 class="card-title" id="tech-2-title">TrueDepth 視線專注追蹤</h4>
          <p class="card-desc" id="tech-2-desc">透過前置原深感測相機即時感知凝神狀態，動態微調環境光影與木香白噪音，助您深度沉浸。</p>
        </div>
        <div class="card">
          <div class="card-icon">💓</div>
          <h4 class="card-title" id="tech-3-title">Apple Watch & HealthKit HRV</h4>
          <p class="card-desc" id="tech-3-desc">讀取心率變異度 (HRV)，解題前後即時呈現自律神經放鬆程度與心流專注指數。</p>
        </div>
        <div class="card">
          <div class="card-icon">🔔</div>
          <h4 class="card-title" id="tech-4-title">432Hz 東方五音冥想聲景</h4>
          <p class="card-desc" id="tech-4-desc">收錄千年古琴、空靈編鐘、深山晨雨與擬真木作觸感回饋，帶來視覺、聽覺與觸覺的三重共振。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Membership Section -->
  <section id="membership">
    <div class="container">
      <div class="section-header">
        <h3 class="section-title" id="tiers-heading">匠人典藏會員方案</h3>
        <p class="section-subtitle" id="tiers-sub">100% 透過 Apple StoreKit 2 訂閱管理，安全透明，隨時於 Apple ID 取消。</p>
      </div>
      <div class="tiers-grid">
        <!-- Monthly -->
        <div class="tier-card">
          <span class="tier-badge monthly" id="tier-1-badge">靈活按月訂閱 · 隨時管理</span>
          <h4 class="tier-title" id="tier-1-title">月度修行方案</h4>
          <ul class="tier-features">
            <li id="tier-1-f1">解鎖全部 3D 魯班鎖與 2D 燕幾圖高階關卡</li>
            <li id="tier-1-f2">每日晨曦定志與夜闌解憂東方音療</li>
            <li id="tier-1-f3">基礎觸控流暢度專注力分析報告</li>
          </ul>
        </div>
        <!-- Annual -->
        <div class="tier-card featured">
          <span class="tier-badge annual" id="tier-2-badge">含免費體驗期 · 依 App Store 優惠同步</span>
          <h4 class="tier-title" id="tier-2-title">年度心流方案 (主要推薦)</h4>
          <ul class="tier-features">
            <li id="tier-2-f1">完整體驗五千年文明長卷與宗師級機關</li>
            <li id="tier-2-f2">解鎖端側 AI 無窮榫卯與殘局生成工坊</li>
            <li id="tier-2-f3">進階 TrueDepth 視線穩定追蹤 & Apple Watch HRV 心流報告</li>
            <li id="tier-2-f4">無限次夜空放天燈祈福與 10 語雅集猜燈謎</li>
          </ul>
        </div>
        <!-- Lifetime -->
        <div class="tier-card">
          <span class="tier-badge lifetime" id="tier-3-badge">贈【和田青玉藏家印信】· 永久解鎖</span>
          <h4 class="tier-title" id="tier-3-title">終身藏家方案</h4>
          <ul class="tier-features">
            <li id="tier-3-f1">一次付清，永久擁有全部五千年歷史章節與未來更新</li>
            <li id="tier-3-f2">獨家獲贈【終身藏家和田青玉印章】落款特權</li>
            <li id="tier-3-f3">包含未來 Apple Vision Pro (visionOS) 空間巨型機關擴充包</li>
            <li id="tier-3-f4">零訂閱壓力，收藏一座靜謐的數字東方工藝博物館</li>
          </ul>
        </div>
      </div>

      <!-- Auto-Renewal Disclosure -->
      <div class="disclosure-box">
        <h4 id="eula-disclosure-title">Apple App Store 訂閱條款與自動續期說明</h4>
        <p id="eula-disclosure-text">付款將在確認購買時自您的 Apple ID 帳戶扣款。訂閱會自動續期，除非在當前計費週期結束前至少 24 小時取消。帳戶將在當前週期結束前 24 小時內收取續期費用。購買後您可隨時至 Apple ID 帳戶設定中管理或取消訂閱。免費試用期內取消將不產生任何費用。</p>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-links">
        <a href="privacy.html" id="footer-privacy">隱私權政策</a>
        <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" target="_blank" rel="noopener" id="footer-eula">Apple 標準許可協議 (Standard EULA)</a>
      </div>
      <p class="footer-contact"><span id="footer-support">支援與聯絡</span>：<a href="mailto:howly7777777@gmail.com" style="color: var(--gold); text-decoration: underline; font-weight: 600;">howly7777777@gmail.com</a></p>
      <p class="footer-copy" id="footer-rights">版權所有 © 2026 心象天工 MindCraft Zen 團隊。保留所有權利。</p>
    </div>
  </footer>

  <script>
    const translations = __TRANSLATIONS_PLACEHOLDER__;

    function applyLanguage(lang) {
      const data = translations[lang] || translations['zh-Hant'];
      document.documentElement.lang = lang;
      
      // Update Texts
      document.getElementById('nav-title').textContent = data.nav_title;
      document.getElementById('nav-subtitle').textContent = data.nav_subtitle;
      document.getElementById('nav-crafts').textContent = data.nav_crafts;
      document.getElementById('nav-tech').textContent = data.nav_tech;
      document.getElementById('nav-tiers').textContent = data.nav_tiers;
      document.getElementById('nav-privacy').textContent = data.nav_privacy;
      document.getElementById('nav-terms').textContent = data.nav_terms;
      if (document.getElementById('nav-support')) document.getElementById('nav-support').textContent = data.nav_support || '✉️ Support';
      if (document.getElementById('footer-support')) document.getElementById('footer-support').textContent = data.footer_support_label || data.footer_support || 'Support';

      document.getElementById('hero-badge').textContent = data.hero_badge;
      document.getElementById('hero-title').textContent = data.hero_title;
      document.getElementById('hero-subtitle').textContent = data.hero_subtitle;
      document.getElementById('hero-cta').textContent = data.hero_cta;
      document.getElementById('hero-cta-sub').textContent = data.hero_cta_sub;

      document.getElementById('crafts-heading').textContent = data.crafts_heading;
      document.getElementById('crafts-sub').textContent = data.crafts_sub;
      document.getElementById('craft-1-title').textContent = data.craft_1_title;
      document.getElementById('craft-1-desc').textContent = data.craft_1_desc;
      document.getElementById('craft-2-title').textContent = data.craft_2_title;
      document.getElementById('craft-2-desc').textContent = data.craft_2_desc;
      document.getElementById('craft-3-title').textContent = data.craft_3_title;
      document.getElementById('craft-3-desc').textContent = data.craft_3_desc;
      document.getElementById('craft-4-title').textContent = data.craft_4_title;
      document.getElementById('craft-4-desc').textContent = data.craft_4_desc;

      document.getElementById('tech-heading').textContent = data.tech_heading;
      document.getElementById('tech-sub').textContent = data.tech_sub;
      document.getElementById('tech-1-title').textContent = data.tech_1_title;
      document.getElementById('tech-1-desc').textContent = data.tech_1_desc;
      document.getElementById('tech-2-title').textContent = data.tech_2_title;
      document.getElementById('tech-2-desc').textContent = data.tech_2_desc;
      document.getElementById('tech-3-title').textContent = data.tech_3_title;
      document.getElementById('tech-3-desc').textContent = data.tech_3_desc;
      document.getElementById('tech-4-title').textContent = data.tech_4_title;
      document.getElementById('tech-4-desc').textContent = data.tech_4_desc;

      document.getElementById('tiers-heading').textContent = data.tiers_heading;
      document.getElementById('tiers-sub').textContent = data.tiers_sub;
      document.getElementById('tier-1-title').textContent = data.tier_1_title;
      document.getElementById('tier-1-badge').textContent = data.tier_1_badge;
      document.getElementById('tier-1-f1').textContent = data.tier_1_feature_1;
      document.getElementById('tier-1-f2').textContent = data.tier_1_feature_2;
      document.getElementById('tier-1-f3').textContent = data.tier_1_feature_3;

      document.getElementById('tier-2-title').textContent = data.tier_2_title;
      document.getElementById('tier-2-badge').textContent = data.tier_2_badge;
      document.getElementById('tier-2-f1').textContent = data.tier_2_feature_1;
      document.getElementById('tier-2-f2').textContent = data.tier_2_feature_2;
      document.getElementById('tier-2-f3').textContent = data.tier_2_feature_3;
      document.getElementById('tier-2-f4').textContent = data.tier_2_feature_4;

      document.getElementById('tier-3-title').textContent = data.tier_3_title;
      document.getElementById('tier-3-badge').textContent = data.tier_3_badge;
      document.getElementById('tier-3-f1').textContent = data.tier_3_feature_1;
      document.getElementById('tier-3-f2').textContent = data.tier_3_feature_2;
      document.getElementById('tier-3-f3').textContent = data.tier_3_feature_3;
      document.getElementById('tier-3-f4').textContent = data.tier_3_feature_4;

      document.getElementById('eula-disclosure-title').textContent = data.eula_disclosure_title;
      document.getElementById('eula-disclosure-text').textContent = data.eula_disclosure_text;

      document.getElementById('footer-privacy').textContent = data.footer_privacy;
      document.getElementById('footer-eula').textContent = data.footer_eula;
      document.getElementById('footer-support').textContent = data.footer_support;
      document.getElementById('footer-rights').textContent = data.footer_rights;

      document.getElementById('lang-select').value = lang;
      localStorage.setItem('mindcraft_lang', lang);
    }

    function changeLanguage(lang) {
      applyLanguage(lang);
    }

    // Auto-detect browser language or read localStorage
    document.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('mindcraft_lang');
      if (savedLang && translations[savedLang]) {
        applyLanguage(savedLang);
        return;
      }
      const navLang = navigator.language || navigator.userLanguage || 'zh-Hant';
      let matched = 'zh-Hant';
      if (navLang.startsWith('zh-CN') || navLang.startsWith('zh-Hans')) matched = 'zh-Hans';
      else if (navLang.startsWith('zh')) matched = 'zh-Hant';
      else if (navLang.startsWith('en')) matched = 'en';
      else if (navLang.startsWith('ja')) matched = 'ja';
      else if (navLang.startsWith('ko')) matched = 'ko';
      else if (navLang.startsWith('de')) matched = 'de';
      else if (navLang.startsWith('fr')) matched = 'fr';
      else if (navLang.startsWith('es')) matched = 'es';
      else if (navLang.startsWith('vi')) matched = 'vi';
      else if (navLang.startsWith('th')) matched = 'th';
      applyLanguage(matched);
    });
  </script>
</body>
</html>
"""

PRIVACY_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="meta-title">隱私權政策 · 心象天工 MindCraft Zen</title>
  <link rel="icon" type="image/png" href="assets/app_icon.png">
  <style>
    :root {
      --bg: #0b0e14;
      --card-bg: rgba(255, 255, 255, 0.04);
      --card-border: rgba(255, 255, 255, 0.09);
      --gold: #d4af37;
      --gold-light: #f5e6a8;
      --cinnabar: #b8332a;
      --text: #f5f5f7;
      --text-muted: rgba(255, 255, 255, 0.65);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans", "Apple SD Gothic Neo", sans-serif;
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }
    a { color: var(--gold); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .container { max-width: 860px; margin: 0 auto; padding: 0 24px; }

    /* Nav */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 14, 20, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--card-border);
    }
    .nav-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 70px;
    }
    .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--gold);
      font-weight: 600;
      font-size: 14px;
    }
    .lang-select {
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
      border: 1px solid var(--card-border);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 13px;
      cursor: pointer;
      outline: none;
    }

    /* Content */
    .privacy-content {
      padding: 60px 0 80px;
    }
    .badge-icon {
      width: 72px;
      height: 72px;
      border-radius: 18px;
      box-shadow: 0 8px 24px rgba(212, 175, 55, 0.25);
      margin-bottom: 24px;
    }
    .date-badge {
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }
    h1 {
      font-size: clamp(26px, 4vw, 36px);
      font-weight: 800;
      color: #fff;
      margin-bottom: 24px;
      line-height: 1.3;
    }
    .summary-card {
      background: rgba(212, 175, 55, 0.07);
      border: 1px solid rgba(212, 175, 55, 0.25);
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 40px;
      font-size: 15px;
      color: var(--gold-light);
      line-height: 1.8;
    }
    .section-block {
      margin-bottom: 36px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 28px;
    }
    h2 {
      font-size: 18px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 8px;
    }
    p {
      font-size: 15px;
      color: rgba(255, 255, 255, 0.85);
      white-space: pre-line;
      line-height: 1.8;
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--card-border);
      padding: 40px 0;
      text-align: center;
      font-size: 13px;
      color: var(--text-muted);
    }
  </style>
</head>
<body>
  <header>
    <div class="container nav-inner">
      <a href="index.html" class="back-btn" id="back-to-home">← 返回首頁</a>
      <select class="lang-select" id="lang-select" onchange="changeLanguage(this.value)">
        <option value="zh-Hant">繁體中文</option>
        <option value="zh-Hans">简体中文</option>
        <option value="en">English</option>
        <option value="ja">日本語</option>
        <option value="ko">한국어</option>
        <option value="de">Deutsch</option>
        <option value="fr">Français</option>
        <option value="es">Español</option>
        <option value="vi">Tiếng Việt</option>
        <option value="th">ไทย</option>
      </select>
    </div>
  </header>

  <main class="privacy-content">
    <div class="container">
      <img src="assets/app_icon.png" alt="MindCraft Zen App Icon" class="badge-icon">
      <div class="date-badge" id="last-updated">最後更新日期：2026 年 10 月 19 日</div>
      <h1 id="title">心象天工 (MindCraft Zen) 隱私權保護政策</h1>

      <div class="summary-card" id="summary">
        我們堅信，隱私是一項基本人權。在《心象天工》中，我們將「極致隱私」融入應用的每一行代碼。本應用遵循 100% 端側運算架構，絕不收集、追蹤、儲存或向任何第三方伺服器傳輸您的個人識別資訊、遊戲進度或生物特徵數據。
      </div>

      <div class="section-block">
        <h2 id="sec-1-title">1. 100% 端側神經網路與數據本地化</h2>
        <p id="sec-1-body"></p>
      </div>

      <div class="section-block">
        <h2 id="sec-2-title">2. TrueDepth 原深感測相機與視線專注追蹤</h2>
        <p id="sec-2-body"></p>
      </div>

      <div class="section-block">
        <h2 id="sec-3-title">3. Apple HealthKit 與心率變異度 (HRV) 數據</h2>
        <p id="sec-3-body"></p>
      </div>

      <div class="section-block">
        <h2 id="sec-4-title">4. Apple StoreKit 2 交易與訂閱安全</h2>
        <p id="sec-4-body"></p>
      </div>

      <div class="section-block">
        <h2 id="sec-5-title">5. 零第三方追蹤與零廣告 SDK</h2>
        <p id="sec-5-body"></p>
      </div>

      <div class="section-block">
        <h2 id="sec-6-title">6. 兒童隱私保護 (COPPA & GDPR-K)</h2>
        <p id="sec-6-body"></p>
      </div>

      <div class="section-block">
        <h2 id="sec-7-title">7. 數據刪除與完全控制權</h2>
        <p id="sec-7-body"></p>
      </div>

      <div class="section-block">
        <h2 id="sec-8-title">8. 條款協議與聯絡支援</h2>
        <p id="sec-8-body"></p>
      </div>
    </div>
  </main>

  <footer>
    <div class="container">
      <p>Copyright © 2026 MindCraft Zen Team. All rights reserved.</p>
    </div>
  </footer>

  <script>
    const privacyTranslations = __PRIVACY_PLACEHOLDER__;

    function applyLanguage(lang) {
      const data = privacyTranslations[lang] || privacyTranslations['zh-Hant'];
      document.documentElement.lang = lang;

      document.getElementById('meta-title').textContent = data.page_title;
      document.getElementById('back-to-home').textContent = data.back_to_home;
      document.getElementById('last-updated').textContent = data.last_updated;
      document.getElementById('title').textContent = data.title;
      document.getElementById('summary').textContent = data.summary;

      document.getElementById('sec-1-title').textContent = data.sec_1_title;
      document.getElementById('sec-1-body').textContent = data.sec_1_body;

      document.getElementById('sec-2-title').textContent = data.sec_2_title;
      document.getElementById('sec-2-body').textContent = data.sec_2_body;

      document.getElementById('sec-3-title').textContent = data.sec_3_title;
      document.getElementById('sec-3-body').textContent = data.sec_3_body;

      document.getElementById('sec-4-title').textContent = data.sec_4_title;
      document.getElementById('sec-4-body').textContent = data.sec_4_body;

      document.getElementById('sec-5-title').textContent = data.sec_5_title;
      document.getElementById('sec-5-body').textContent = data.sec_5_body;

      document.getElementById('sec-6-title').textContent = data.sec_6_title;
      document.getElementById('sec-6-body').textContent = data.sec_6_body;

      document.getElementById('sec-7-title').textContent = data.sec_7_title;
      document.getElementById('sec-7-body').textContent = data.sec_7_body;

      document.getElementById('sec-8-title').textContent = data.sec_8_title;
      document.getElementById('sec-8-body').textContent = data.sec_8_body;

      document.getElementById('lang-select').value = lang;
      localStorage.setItem('mindcraft_lang', lang);
    }

    function changeLanguage(lang) {
      applyLanguage(lang);
    }

    document.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('mindcraft_lang');
      if (savedLang && privacyTranslations[savedLang]) {
        applyLanguage(savedLang);
        return;
      }
      const navLang = navigator.language || navigator.userLanguage || 'zh-Hant';
      let matched = 'zh-Hant';
      if (navLang.startsWith('zh-CN') || navLang.startsWith('zh-Hans')) matched = 'zh-Hans';
      else if (navLang.startsWith('zh')) matched = 'zh-Hant';
      else if (navLang.startsWith('en')) matched = 'en';
      else if (navLang.startsWith('ja')) matched = 'ja';
      else if (navLang.startsWith('ko')) matched = 'ko';
      else if (navLang.startsWith('de')) matched = 'de';
      else if (navLang.startsWith('fr')) matched = 'fr';
      else if (navLang.startsWith('es')) matched = 'es';
      else if (navLang.startsWith('vi')) matched = 'vi';
      else if (navLang.startsWith('th')) matched = 'th';
      applyLanguage(matched);
    });
  </script>
</body>
</html>
"""

def main():
    out_dir = "/Volumes/Vajra Howly/Antigravity APP/20261016/mindcraft"
    os.makedirs(out_dir, exist_ok=True)

    index_html = INDEX_HTML_TEMPLATE.replace(
        "__TRANSLATIONS_PLACEHOLDER__", json.dumps(INDEX_DATA, ensure_ascii=False)
    )
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Generated:", os.path.join(out_dir, "index.html"))

    privacy_html = PRIVACY_HTML_TEMPLATE.replace(
        "__PRIVACY_PLACEHOLDER__", json.dumps(PRIVACY_DATA, ensure_ascii=False)
    )
    with open(os.path.join(out_dir, "privacy.html"), "w", encoding="utf-8") as f:
        f.write(privacy_html)
    print("Generated:", os.path.join(out_dir, "privacy.html"))

if __name__ == "__main__":
    main()
