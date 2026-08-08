TITLE = {"en": "Contact - MacroPhotonic Lab", "cn": "联系方式 - MacroPhotonic Lab"}
NAV_ACTIVE = "contact"

HEAD_EXTRA = '    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />'

CSS = """
        .contact-layout {
            display: flex;
            gap: 40px;
            align-items: flex-start;
        }

        .contact-list {
            flex: 0 0 260px;
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .contact-row {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 12px 18px;
            border-radius: 10px;
            transition: background 0.2s;
        }

        .contact-row:first-child {
            padding-top: 0;
        }

        .contact-row:hover {
            background: #F8FAFC;
        }

        .contact-row .icon {
            font-size: 22px;
            width: 28px;
            text-align: center;
            flex-shrink: 0;
        }

        .contact-row .label {
            font-size: 14px;
            color: #64748B;
            min-width: 50px;
            flex-shrink: 0;
        }

        .contact-row .value {
            font-size: 16px;
            color: #1E3A8A;
            font-weight: 500;
        }

        .contact-row .value a {
            color: #1E3A8A;
            text-decoration: none;
            transition: color 0.2s;
        }

        .contact-row .value a:hover {
            color: #3B82F6;
        }

        .map-wrapper {
            flex: 1;
            aspect-ratio: 1;
        }

        #map {
            width: 100%;
            height: 100%;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
        }

        @media (max-width: 768px) {
            .page-title { font-size: 24px; }
            .contact-layout {
                flex-direction: column;
                gap: 24px;
            }
            .contact-list { flex: 1; }
            .map-wrapper { aspect-ratio: 4/3; width: 100%; }
            #map { min-height: 250px; }
        }

        @media (max-width: 480px) {
            .map-wrapper { aspect-ratio: 4/3; }
            #map { min-height: 200px; }
        }
"""

BODY = """
    <div class="container">
        <div class="card">
            <h3 class="page-title" id="contact-title-en">Contact</h3>
            <h3 class="page-title" id="contact-title-cn" style="display: none;">联系方式</h3>

            <div class="contact-layout">
                <div class="contact-list">
                    <div class="contact-row">
                        <span class="icon">📧</span>
                        <span class="label" id="email-label-en">Email</span>
                        <span class="label" id="email-label-cn" style="display: none;">邮箱</span>
                        <span class="value">
                            <a href="mailto:majw@sustech.edu.cn">majw@sustech.edu.cn</a>
                        </span>
                    </div>
                    <div class="contact-row">
                        <span class="icon">🔗</span>
                        <span class="label" id="links-label-en">Links</span>
                        <span class="label" id="links-label-cn" style="display: none;">链接</span>
                        <span class="value">
                            <a href="https://scholar.google.com/citations?user=-2sAiXwAAAAJ&hl=en" target="_blank">Google Scholar</a>
                        </span>
                    </div>
                    <div class="contact-row">
                        <span class="icon">📍</span>
                        <span class="label" id="addr-label-en">Address</span>
                        <span class="label" id="addr-label-cn" style="display: none;">地址</span>
                        <span class="value" id="addr-value-en">No. 1088 Xueyuan Road, Nanshan District, Shenzhen 518055, China</span>
                        <span class="value" id="addr-value-cn" style="display: none;">中国广东省深圳市南山区学苑大道1088号，邮编 518055</span>
                    </div>
                </div>

                <div class="map-wrapper">
                    <div id="map"></div>
                </div>
            </div>
        </div>
    </div>
"""

SCRIPT = """
        var s = document.createElement('script');
        s.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
        s.onload = function() {
            var lat = 22.602579, lng = 113.990844;
            var map = L.map('map').setView([lat, lng], 17);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
                maxZoom: 19
            }).addTo(map);
            L.marker([lat, lng]).addTo(map);

            window.addEventListener('resize', function() {
                map.invalidateSize();
            });
        };
        document.head.appendChild(s);
"""
