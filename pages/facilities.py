TITLE = {"en": "Facilities - MacroPhotonic Lab", "cn": "实验设备 - MacroPhotonic Lab"}
NAV_ACTIVE = "facilities"

CSS = """
        .facility-section {
            margin-bottom: 56px;
        }

        .facility-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 28px;
            width: 100%;
        }

        .nano-fabrication-grid {
            grid-template-columns: 1fr !important;
        }

        .facility-card {
            background: #ffffff;
            border: 1px solid #F1F5F9;
            border-radius: 12px;
        }

        .facility-img {
            width: 80%;
            max-width: 80%;
            margin: 0 auto;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(30, 58, 138, 0.08);
            background: #F5F7FA;
            padding: 8px;
        }

        .facility-img img {
            width: 100%;
            height: auto;
            display: block;
            object-fit: contain;
        }

        .facility-info {
            padding: 20px;
        }

        .facility-name {
            font-size: 18px;
            font-weight: 600;
            color: #1E3A8A;
            margin-bottom: 12px;
        }

        .facility-desc {
            font-size: 15px;
            color: #374151;
            line-height: 1.7;
        }

        .facility-desc a {
            color: #3B82F6;
            text-decoration: none;
            font-weight: 500;
        }

        .facility-desc a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .page-title { font-size: 24px; }
            .section-subtitle { font-size: 20px; }
            .facility-img { width: 90%; max-width: 90%; }
            .facility-grid { grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; }
        }

        @media (max-width: 600px) {
            .facility-grid { grid-template-columns: 1fr; }
            .facility-img { width: 95%; max-width: 95%; }
            .facility-info { padding: 16px; }
            .facility-desc { word-break: break-word; hyphens: auto; }
        }

        @media (max-width: 375px) {
            .facility-name { font-size: 17px; }
            .facility-desc { font-size: 14px; word-break: break-word; }
        }
"""

BODY = """
    <div class="container">
        <div class="card">
            <div class="facility-section">
                <h3 class="page-title" id="nano-title-en">Nano-Fabrication</h3>
                <h3 class="page-title" id="nano-title-cn" style="display: none;">微纳加工平台</h3>

                <div class="facility-grid nano-fabrication-grid">
                    <div class="facility-card hover-card">
                        <div class="facility-img">
                            <img src="images/facility/nano-fabrication.jpg" alt="nano-fabrication" loading="lazy">
                        </div>
                        <div class="facility-info">
                            <div class="facility-name" id="nano-name-en">SUSTech Core Research Facilities (CRF)</div>
                            <div class="facility-name" id="nano-name-cn" style="display: none;">南方科技大学分析检测中心</div>

                            <div class="facility-desc" id="nano-desc-en">
                                Most of our devices—photonic crystals, microcavities, integrated photonic chips, and NEMS—can be fabricated in the SUSTech Core Research Facilities (CRF), which provides a complete nanofabrication chain: pattern definition (electron-beam and photolithography), thin-film deposition (PECVD, LPCVD, ALD), and etching (ICP-RIE). For more details, please visit <a href="https://crf.sustech.edu.cn/platform/weina" target="_blank">the official website</a>.
                            </div>
                            <div class="facility-desc" id="nano-desc-cn" style="display: none;">
                                我们的光子晶体、微腔、集成光子芯片与纳米机电等器件大部分可在南方科技大学分析检测中心制备。该平台覆盖完整微纳加工工艺链：图形化（电子束光刻、光刻）、薄膜沉积（PECVD、LPCVD、ALD）与刻蚀（ICP-RIE）等。更多详情请访问 <a href="https://crf.sustech.edu.cn/platform/weina" target="_blank">官方网站</a>。
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="facility-section">
                <h3 class="page-title" id="opto-title-en">Optoelectronic Characterization</h3>
                <h3 class="page-title" id="opto-title-cn" style="display: none;">光电表征平台</h3>

                <div class="facility-grid">
                    <div class="facility-card hover-card">
                        <div class="facility-info">
                            <div class="facility-name" id="meta-name-en">Meta-surface and quantum matter characterization</div>
                            <div class="facility-name" id="meta-name-cn" style="display: none;">超表面与量子物态表征系统</div>

                            <div class="facility-desc" id="meta-desc-en">
                                For characterizing photonic nano-structures, quantum materials, and hybrid light-matter quantum states across nearly all photonic degrees of freedom, with ultrafast time resolution of 100 fs.<br>
                                Key facilities include:<br>
                                • Custom angle-resolved microscope<br>
                                • Transient pump-probe system (under construction)<br>
                                • High-resolution spectrometer & single-photon detection setup<br>
                                • Piezo scanning stages, lock-in amplifier, cryostat
                            </div>
                            <div class="facility-desc" id="meta-desc-cn" style="display: none;">
                                用于表征光子纳米结构、量子材料及光-物质杂化量子态，覆盖光子几乎所有自由度，时间分辨率可达 100 飞秒。<br>
                                核心设备包括：<br>
                                • 定制化角分辨显微镜<br>
                                • 瞬态泵浦探测系统（搭建中）<br>
                                • 高分辨率光谱仪及单光子探测系统<br>
                                • 压电扫描台、锁相放大器、低温恒温器
                            </div>
                        </div>
                    </div>

                    <div class="facility-card hover-card">
                        <div class="facility-info">
                            <div class="facility-name" id="laser-name-en">III-V semiconductor laser characterization</div>
                            <div class="facility-name" id="laser-name-cn" style="display: none;">III-V族半导体激光器表征系统</div>

                            <div class="facility-desc" id="laser-desc-en">
                                For characterizing optical/electrical pumped semiconductor lasers at communication bands. Key facilities include:<br>
                                • Pump lasers (high power ns laser)<br>
                                • High-power electrical source<br>
                                • Infrared spectrometer (Andor Kymera + iDus CCD)<br>
                                • Infrared CMOS camera (Hamamatsu)<br>
                                • g2 measurement system
                            </div>
                            <div class="facility-desc" id="laser-desc-cn" style="display: none;">
                                用于表征通信波段的光泵浦/电泵浦半导体激光器。核心设备包括：<br>
                                • 泵浦激光器（高功率纳秒激光器）<br>
                                • 高功率电信号源<br>
                                • 红外光谱仪（Andor Kymera + iDus CCD）<br>
                                • 红外CMOS相机（滨松）<br>
                                • g2测量系统
                            </div>
                        </div>
                    </div>

                    <div class="facility-card">
                        <div class="facility-info">
                            <div class="facility-name" id="phonon-name-en">Nano-mechanics and on-chip phonon characterization</div>
                            <div class="facility-name" id="phonon-name-cn" style="display: none;">纳米力学与片上声子表征系统</div>

                            <div class="facility-desc" id="phonon-desc-en">
                                This characterization platform is currently being established. More details will be updated soon.
                            </div>
                            <div class="facility-desc" id="phonon-desc-cn" style="display: none;">
                                该表征平台正在建设中，详细信息将尽快更新。
                            </div>
                        </div>
                    </div>

                    <div class="facility-card hover-card">
                        <div class="facility-info">
                            <div class="facility-name" id="chip-name-en">Photonic chip testing system</div>
                            <div class="facility-name" id="chip-name-cn" style="display: none;">光子芯片测试系统</div>

                            <div class="facility-desc" id="chip-desc-en">
                                This characterization platform is currently being established. More details will be updated soon.
                            </div>
                            <div class="facility-desc" id="chip-desc-cn" style="display: none;">
                                该表征平台正在建设中，详细信息将尽快更新。
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

SCRIPT = ""
