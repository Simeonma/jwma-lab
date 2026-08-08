TITLE = {"en": "Publications - MacroPhotonic Lab", "cn": "发表论文 - MacroPhotonic Lab"}
NAV_ACTIVE = "publications"

CSS = """
        .title-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 32px;
            padding-bottom: 16px;
            border-bottom: 2px solid #E2E8F0;
        }

        .card h3 {
            font-size: 28px;
            color: #1E3A8A;
        }

        .scholar-button {
            padding: 8px 16px;
            background: #1E3A8A;
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 500;
            white-space: nowrap;
            transition: all 0.2s ease;
        }

        .scholar-button:hover {
            opacity: 0.9;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(30, 58, 138, 0.15);
        }

        .year-timeline {
            position: relative;
            padding-left: 48px;
            margin-bottom: 16px;
        }

        .year-timeline::before {
            content: '';
            position: absolute;
            left: 12px;
            top: 0;
            bottom: 0;
            width: 2px;
            background-color: #E2E8F0;
            z-index: 1;
        }

        .year {
            font-size: 22px;
            font-weight: 600;
            color: #1E3A8A;
            margin-bottom: 24px;
            position: relative;
            padding-left: 16px;
            display: inline-block;
            cursor: pointer;
            user-select: none;
        }

        .year::before {
            content: '';
            position: absolute;
            left: -40px;
            top: 50%;
            transform: translateY(-50%);
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background-color: #3B82F6;
            border: 4px solid #F8FAFC;
            box-shadow: 0 0 0 2px #3B82F6;
            z-index: 2;
            transition: transform 0.2s ease;
        }

        .year:hover::before {
            transform: translateY(-50%) scale(1.2);
        }

        .year::after {
            content: ' \\25B2';
            font-size: 14px;
            opacity: 0.6;
        }

        .year.collapsed::after {
            content: ' \\25BC';
        }

        .year-group {
            margin-bottom: 60px;
        }

        .year-group.collapsed .pub-item,
        .year-group.collapsed .year-timeline::before {
            display: none;
        }

        .year-group.collapsed .year-timeline {
            margin-bottom: 0;
        }

        .year-group.collapsed {
            margin-bottom: 24px;
        }

        .pub-item {
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #E2E8F0;
            position: relative;
            padding-left: 8px;
        }

        .pub-item.has-img {
            display: flex;
            flex-direction: column;
            gap: 16px;
            align-items: center;
        }

        .pub-img-container {
            position: relative;
            width: 80%;
            max-width: 80%;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(30, 58, 138, 0.08);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .pub-img {
            width: 100%;
            height: auto;
            display: block;
        }

        .pub-desc {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: auto;
            max-height: 80%;
            background: rgba(0, 0, 0, 0.8);
            color: #ffffff;
            padding: 20px 24px;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            display: block !important;
            white-space: normal !important;
            overflow-wrap: break-word !important;
            line-height: 1.6;
            font-size: 16px;
            overflow-y: auto;
            flex: none !important;
            align-items: normal !important;
            pointer-events: none;
        }

        .pub-desc a {
            color: #93C5FD;
            font-weight: 500;
            text-decoration: none;
            display: inline !important;
            white-space: normal !important;
            word-break: break-word !important;
            pointer-events: auto;
        }

        .pub-desc a:hover {
            text-decoration: underline;
        }

        .pub-img-container:hover .pub-desc {
            opacity: 1;
            visibility: visible;
        }

        .pub-img-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(30, 58, 138, 0.12);
        }

        /* Click-to-toggle state for mobile */
        .pub-img-container.show-desc .pub-desc {
            opacity: 1;
            visibility: visible;
        }

        .pub-item.no-img {
            display: block;
        }

        .pub-content {
            flex: 1;
            width: 100%;
        }

        .pub-title {
            font-size: 20px;
            font-weight: 600;
            color: #1E3A8A;
            margin-bottom: 5px;
            line-height: 1.5;
        }

        .pub-title a {
            color: #1E3A8A;
            text-decoration: none;
            transition: all 0.2s ease;
        }

        .pub-title a:hover {
            color: #3B82F6;
            text-decoration: underline;
        }

        .pub-authors {
            font-size: 16px;
            color: #4B5563;
            margin-bottom: 5px;
            line-height: 1.5;
        }

        .pub-journal {
            font-size: 16px;
            font-style: italic;
            font-weight: 600;
            color: #1F2937;
            margin-bottom: 5px;
            display: inline;
            margin-left: 0px;
        }

        @media (max-width: 768px) {
            .card h3 { font-size: 24px; }
            .year-timeline { padding-left: 40px; }
            .year::before { left: -34px; width: 12px; height: 12px; }
            .pub-img-container { width: 90%; max-width: 90%; }
            .pub-desc { font-size: 15px; padding: 16px 20px; max-height: 90%; }
            .pub-title { font-size: 18px; }
        }

        @media (max-width: 600px) {
            .title-row { flex-direction: column; align-items: flex-start; gap: 12px; }
            .year-timeline { padding-left: 34px; }
            .year::before { left: -29px; width: 10px; height: 10px; }
            .pub-img-container { width: 95%; max-width: 95%; }
            .pub-desc { font-size: 14px; padding: 12px 16px; max-height: 90%; }
        }

        @media (max-width: 375px) {
            .pub-title { font-size: 17px; }
            .pub-authors { font-size: 15px; }
            .year-timeline { padding-left: 30px; }
            .year::before { left: -26px; }
        }
"""

BODY = """
    <div class="container">
        <div class="card">
            <div class="title-row">
                <h3 id="pub-title-en">Selected Publications</h3>
                <h3 id="pub-title-cn" style="display: none;">Selected Publications</h3>
                <a href="https://scholar.google.com/citations?user=-2sAiXwAAAAJ&hl=en" class="scholar-button" target="_blank">
                    <span id="scholar-btn-en">Full Publications in Google Scholar</span>
                    <span id="scholar-btn-cn" style="display: none;">Full Publications in Google Scholar</span>
                </a>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2026-en" onclick="toggleYear(this)">2026</div>
                    <div class="year" id="year-2026-cn" style="display: none;" onclick="toggleYear(this)">2026</div>

                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/Supersolids_at_room_temperature.jpg" alt="Supersolids at room temperature" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                Supersolids are an exotic macroscopic quantum phase that exists in ultracold atomic gases and III-V semiconductors at cryogenic temperatures. We experimentally demonstrate <strong>exciton-polariton supersolids at room temperature</strong>.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.21203/rs.3.rs-9177620/v1" target="_blank">Room-temperature polariton supersolids</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>*; Yuanhao Gong*; Shuang Zhang; Xiaobo Yin&dagger;; Xiang Zhang&dagger;.
                                <span class="pub-journal">Research Square (preprint)</span> (2026)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/Excitonic negative refraction mediated by magnetic orders.jpg" alt="Excitonic negative refraction mediated by magnetic orders" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                We report the first <strong>excitonic negative refraction</strong>. This work is featured in <a href="https://phys.org/news/2026-02-nanoengineers-chip-excitonic-hyperlens.html" target="_blank">Phys.org</a>, <a href="https://www.miragenews.com/scientists-discover-natural-magnetic-materials-1611657/" target="_blank">Mirage News</a>, <a href="https://www.eurekalert.org/news-releases/1115460" target="_blank">EurekAlert!</a>, <a href="https://news.sciencenet.cn/htmlnews/2026/1/559084.shtm" target="_blank">Sciencenet (科学网)</a>, <a href="https://www.stheadline.com/zh-hans/edu-news/3540828/%E6%B8%AF%E5%A4%A7%E7%A0%94%E7%A9%B6%E6%8F%AD%E7%A4%BA%E8%B4%9F%E6%8A%98%E5%B0%84-%E5%88%B6%E5%BE%AE%E5%9E%8B%E6%BF%80%E5%AD%90%E8%B6%85%E9%80%8F%E9%95%9C" target="_blank">星島頭條</a>, <a href="https://news.mingpao.com/pns/%E6%95%99%E8%82%B2/article/20260202/s00011/1769966776846/%E6%B8%AF%E5%A4%A7%E7%A0%94%E6%BF%80%E5%AD%90%E8%B6%85%E9%80%8F%E9%95%9C-%E6%93%8D%E6%8E%A7%E5%85%89%E3%80%8C%E8%BD%89%E5%BD%8E%E3%80%8D%E5%88%B0%E5%85%89%E3%80%8C%E8%B6%85%E9%80%8F%E9%95%9C%E3%80%8D" target="_blank">明報</a>.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1038/s41565-025-02118-5" target="_blank">Excitonic negative refraction mediated by magnetic orders</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>*; Xiong Wang*; Yuanhao Gong; Chong Hu; Qi Wang; Kai Feng; Zemeng Lin; Teruya Ishihara; Xiaobo Yin; Shuang Zhang; Zuxin Chen&dagger; Xiaoze Liu&dagger; Xiaodong Cui; Xiang Zhang&dagger;.
                                <span class="pub-journal">Nature Nanotechnology</span>, 21, 374-379 (2026)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1002/lpor.202501208" target="_blank">Monolayer J-aggregate crystals strong coupling with an all-dielectric metasurface for photonic properties modification</a>
                            </div>
                            <div class="pub-authors">
                                Xinyi Zhao; <strong>Jingwen Ma</strong>; Fuhuan Shen&dagger;; Xiaokun Guo; Zefeng Chen&dagger;; Jianbin Xu&dagger;.
                                <span class="pub-journal">Laser &amp; Photonics Reviews</span>, 20, 2, e01208 (2026)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2025-en" onclick="toggleYear(this)">2025</div>
                    <div class="year" id="year-2025-cn" style="display: none;" onclick="toggleYear(this)">2025</div>
                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/topological parametric phonon oscillator.jpg" alt="topological_paramatric_phonon_oscillator" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                Interacting topological bosonic systems exhibit fundamentally distinct behaviour to their fermionic counterparts. We report the first <strong>topological parametric oscillators</strong> based on a Dirac-vortex nano-electro-mechanical cavity.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1002/adma.202309015" target="_blank">A topological parametric phonon oscillator</a>
                            </div>
                            <div class="pub-authors">
                                Xiang Xi*; <strong>Jingwen Ma</strong>*; Xiankai Sun&dagger;.
                                <span class="pub-journal">Advanced Materials</span>, 37, 2, 2309015 (2025)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1126/science.adw1922" target="_blank">Stacking the future of heterogeneous optoelectronics</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>; Xiaobo Yin.
                                <span class="pub-journal">Science</span>, 387, eadw1922 (2025) [Invited expert voices]
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1002/lpor.202502392" target="_blank">Hybrid cavity from tunable coupling between anapole and Fabry-Perot resonance or anti-resonance</a>
                            </div>
                            <div class="pub-authors">
                                Aoning Luo; Haitao Li; Ken Qin; <strong>Jingwen Ma</strong>; Shijie Kang; Jiayu Fan; Yiyi Yao; Xiexuan Zhang; Jiusi Yu; BoYang&dagger; Qu; Xiaoxiao Wu&dagger;.
                                <span class="pub-journal">Laser &amp; Photonics Reviews</span>, e02392 (2025)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1103/bzpw-7h2x" target="_blank">Far-field excitation of a photonic flat band via a tailored anapole mode</a>
                            </div>
                            <div class="pub-authors">
                                Peiwen Ren*; Junrong Zheng*; Zhuo Huang*; Yan Liu; Long Zhang; Hua Zhang; <strong>Jingwen Ma</strong>; Zhanghai Chen&dagger;; Jian-Feng Li&dagger;; Jun Yi&dagger;; Zhilin Yang&dagger;.
                                <span class="pub-journal">Physical Review Letters</span>, 135, 083803 (2025)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1103/PhysRevLett.134.196601" target="_blank">Boundary-induced topological chiral extended states in Weyl metamaterial waveguides</a>
                            </div>
                            <div class="pub-authors">
                                Ning Han; Fujia Chen; Mingzhu Li; Rui Zhao; Wenhao Li; Qiaolu Chen; Li Zhang; Yuang Pan; Yuze Hu; Mingyu Tong; Lu Qi; <strong>Jingwen Ma</strong>; Zhi-Ming Yu; Hongsheng Chen&dagger;; Yihao Yang&dagger;.
                                <span class="pub-journal">Physical Review Letters</span>, 134, 196601 (2025)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2024-en" onclick="toggleYear(this)">2024</div>
                    <div class="year" id="year-2024-cn" style="display: none;" onclick="toggleYear(this)">2024</div>
                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/vortex_string_chiral_mode.jpg" alt="vortex_string_chiral_mode" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                Vortex strings are hypothetical topological defects in the geometry of spacetime in cosmology. We report the first <strong>experimental observations of vortex string chiral modes</strong> using a meta-material system.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1038/s41467-024-46641-w" target="_blank">Observation of vortex-string chiral modes in metamaterials</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>; Ding Jia; Li Zhang; Yi-jun Guan; Yong Ge; Hong-xiang Sun&dagger;; Shou-qi Yuan; Hongsheng Chen; Yihao Yang&dagger;; Xiang Zhang&dagger;.
                                <span class="pub-journal">Nature Communications</span>, 15, 2332 (2024)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1093/nsr/nwae275" target="_blank">Parity-time and anti-parity-time symmetries in heat transfer</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>; Xiang Zhang; Xiaobo Yin&dagger;.
                                <span class="pub-journal">National Science Review</span>, 11, 9, nwae275 (2024) [Invited Commentary]
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1002/lpor.202300584" target="_blank">Tunable Kerker scattering in a self-coupled polaritonic metasurface</a>
                            </div>
                            <div class="pub-authors">
                                Fuhuan Shen; Yaoqiang Zhou; <strong>Jingwen Ma</strong>; Jiapeng Zheng; Jianfang Wang; Zefeng Chen&dagger;; Jianbin Xu&dagger;.
                                <span class="pub-journal">Laser &amp; Photonics Reviews</span>, 18, 1, 2300584 (2024)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2023-en" onclick="toggleYear(this)">2023</div>
                    <div class="year" id="year-2023-cn" style="display: none;" onclick="toggleYear(this)">2023</div>
                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/Room-temperature continuous-wave Dirac-vortex topological lasers on silicon.png" alt="Dirac-vortex lasers" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                We report the first Dirac-vortex microcavity laser that harnesses an auxiliary orbital degree of freedom. This work is featured in <a href="https://doi.org/10.1038/s41377-024-01398-1" target="_blank">Light: Science &amp; Applications 13, 64 (2024)</a>, <a href="https://phys.org/news/2023-10-room-temperature-continuous-wave-topological-dirac-vortex-microcavity.html" target="_blank">Phys.org</a>, and <a href="https://paper.sciencenet.cn/htmlpaper/2023/12/202312261443226192329.shtm" target="_blank">Sciencenet (科学网)</a>.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1038/s41377-023-01290-4" target="_blank">Room-temperature continuous-wave Dirac-vortex topological lasers on silicon</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>*; Taojie Zhou*; Mingchu Tang*; Haochuan Li; Zhan Zhang; Xiang Xi; Mickael Martin; Thierry Baron; Huiyun Liu; Zhaoyu Zhang&dagger;; Siming Chen&dagger;; Xiankai Sun&dagger;.
                                <span class="pub-journal">Light: Science &amp; Applications</span>, 12, 255 (2023)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1021/acsnano.3c07993" target="_blank">Exciton polaritons in emergent two-dimensional semiconductors</a>
                            </div>
                            <div class="pub-authors">
                                Haifeng Kang; <strong>Jingwen Ma</strong>&dagger;; Junyu Li; Xiang Zhang&dagger;; Xiaoze Liu&dagger;.
                                <span class="pub-journal">ACS Nano</span>, 17, 24, 24449-4467 (2023)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1088/1361-6633/ac953e" target="_blank">2D-materials-integrated optoelectromechanics: recent progress and future perspectives</a>
                            </div>
                            <div class="pub-authors">
                                Mingzeng Peng; Jiadong Cheng; Xinhe Zheng; <strong>Jingwen Ma</strong>; Ziyao Feng; Xiankai Sun&dagger;.
                                <span class="pub-journal">Reports on Progress in Physics</span>, 86, 2, 26402 (2023)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2022-en" onclick="toggleYear(this)">2022</div>
                    <div class="year" id="year-2022-cn" style="display: none;" onclick="toggleYear(this)">2022</div>
                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1021/acsphotonics.2c00711" target="_blank">Monolithically integrated ultralow threshold topological corner state nanolasers on silicon</a>
                            </div>
                            <div class="pub-authors">
                                Taojie Zhou*; <strong>Jingwen Ma</strong>*; Mingchu Tang*; Haochuan Li; Mickael Martin; Thierry Baron; Huiyun Liu; Siming Chen&dagger;; Xiankai Sun&dagger;; Zhaoyu Zhang&dagger;.
                                <span class="pub-journal">ACS Photonics</span>, 9, 12, 3824-3830 (2022)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1038/s41467-022-33088-0" target="_blank">Transition metal dichalcogenide metaphotonic and self-coupled polaritonic platform grown by chemical vapor deposition</a>
                            </div>
                            <div class="pub-authors">
                                Fuhuan Shen; Zhenghe Zhang; Yaoqiang Zhou; <strong>Jingwen Ma</strong>; Kun Chen; Huanjun Chen; Shaojun Wang; Jianbin Xu&dagger;; Zefeng Chen&dagger;.
                                <span class="pub-journal">Nature Communications</span>, 13, 5597 (2022)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1364/PRJ.451344" target="_blank">Terahertz topological photonic waveguide switch for on-chip communication</a>
                            </div>
                            <div class="pub-authors">
                                Xudong Liu; Jialiang Huang; Hao Chen; Zhengfang Qian; <strong>Jingwen Ma</strong>; Xiankai Sun&dagger;; Shuting Fan; Yiwen Sun&dagger;.
                                <span class="pub-journal">Photonics Research</span>, 10, 4, 1090-1096 (2022)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2021-en" onclick="toggleYear(this)">2021</div>
                    <div class="year" id="year-2021-cn" style="display: none;" onclick="toggleYear(this)">2021</div>
                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/Nanomechanical topological insulators with an auxiliary orbital degree of freedom.jpg" alt="Nanomechanical topological insulators" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                We report an topological system with auxiliary orbital degree of freedom. This work is featured in <a href="https://doi.org/10.1038/s41565-021-00853-z" target="_blank">Nature Nanotechnology 16 (5): 487-489 (2021)</a>.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1038/s41565-021-00868-6" target="_blank">Nanomechanical topological insulators with an auxiliary orbital degree of freedom</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>*; Xiang Xi*; Yuan Li; Xiankai Sun&dagger;.
                                <span class="pub-journal">Nature Nanotechnology</span>, 16, 5, 576-583 (2021)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1002/adma.202006521" target="_blank">Experimental demonstration of dual-band nanoelectromechanical valley-Hall topological metamaterials</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>*; Xiang Xi*; Xiankai Sun&dagger;.
                                <span class="pub-journal">Advanced Materials</span>, 33, 10, 2006521 (2021)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1126/sciadv.abe1398" target="_blank">Observation of chiral edge states in gapped nanomechanical graphene</a>
                            </div>
                            <div class="pub-authors">
                                Xiang Xi*; <strong>Jingwen Ma</strong>*; Shuai Wan; Chun-Hua Dong; Xiankai Sun&dagger;.
                                <span class="pub-journal">Science Advances</span>, 7, 2, eabe1398 (2021) [This work is featured in <a href="https://phys.org/news/2021-01-chiral-edge-states-gapped-nanomechanical.html" target="_blank">Phys.org</a> and <a href="https://statnano.com/world-news/84432/Observing-chiral-edge-states-in-gapped-nanomechanical-graphene" target="_blank">StatNano</a>]
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1364/OPTICA.423877" target="_blank">Experimental investigation of the angular symmetry of optical force in a solid dielectric</a>
                            </div>
                            <div class="pub-authors">
                                Xiang Xi; <strong>Jingwen Ma</strong>; Zhong-Hao Zhou; Xin-Xin Hu; Yuan Chen; Chang-Ling Zou&dagger;; Chun-Hua Dong&dagger;; Xiankai Sun&dagger;.
                                <span class="pub-journal">Optica</span>, 8, 11, 1435-1441 (2021)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2019-en" onclick="toggleYear(this)">2019</div>
                    <div class="year" id="year-2019-cn" style="display: none;" onclick="toggleYear(this)">2019</div>
                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/Topological photonic integrated circuits based on valley kink states.jpg" alt="Valley kink states" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                We demonstrate topological photonic integrated circuits. This work is featured as cover article.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1002/lpor.201900087" target="_blank">Topological photonic integrated circuits based on valley kink states</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>; Xiang Xi; Xiankai Sun&dagger;.
                                <span class="pub-journal">Laser &amp; Photonics Reviews</span>, 13, 12, 1900087 (2019)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1364/OE.27.038087" target="_blank">Amplification of 18 OAM modes in a ring-core Erbium-doped fiber with low differential modal gain</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>*; Fei Xia*; Shi Chen*; Jian Wang&dagger;.
                                <span class="pub-journal">Optics Express</span>, 27, 26, 38087-38097 (2019)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1109/JSTQE.2019.2914413" target="_blank">Optically controlled topologically protected acoustic wave amplification</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>; Ziyao Feng; Yuan Li; Xiankai Sun&dagger;.
                                <span class="pub-journal">IEEE Journal of Selected Topics in Quantum Electronics</span>, 26, 5, 1-10 (2019)
                            </div>
                        </div>
                    </div>

                    <div class="pub-item no-img">
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1364/OPTICA.6.001342" target="_blank">Photonic integrated circuits with bound states in the continuum</a>
                            </div>
                            <div class="pub-authors">
                                Zejie Yu; Xiang Xi; <strong>Jingwen Ma</strong>; Hon Ki Tsang; Chang-Ling Zou; Xiankai Sun&dagger;.
                                <span class="pub-journal">Optica</span>, 6, 10, 1342-1348 (2019)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="year-group">
                <div class="year-timeline">
                    <div class="year" id="year-2016-en" onclick="toggleYear(this)">2016</div>
                    <div class="year" id="year-2016-cn" style="display: none;" onclick="toggleYear(this)">2016</div>
                    <div class="pub-item has-img">
                        <div class="pub-img-container" onclick="togglePubDesc(this)">
                            <img src="images/publications/graphene_isolator.jpg" alt="graphene_isolator" loading="lazy" class="pub-img">
                            <div class="pub-desc">
                                We propose a new design of on-chip isolator using photonic spin-orbit interaction. This work is featured as cover article and selected by Optics &amp; Photonics News (OPN), The optical Society's monthly news magazine, as one of <a href="https://www.optica-opn.org/home/articles/volume_27/december_2016/features/optics_in_2016/" target="_blank">the world's 30 most clearly communicated breakthroughs in optics in 2016</a>.
                            </div>
                        </div>
                        <div class="pub-content">
                            <div class="pub-title">
                                <a href="https://doi.org/10.1063/1.4945715" target="_blank">Hybrid graphene/silicon integrated optical isolators with photonic spin-orbit interaction</a>
                            </div>
                            <div class="pub-authors">
                                <strong>Jingwen Ma</strong>; Xiang Xi; Zejie Yu; Xiankai Sun&dagger;.
                                <span class="pub-journal">Applied Physics Letters</span>, 108, 15, 151103 (2016)
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

SCRIPT = """
        function toggleYear(el) {
            var group = el.closest('.year-group');
            group.classList.toggle('collapsed');
            el.classList.toggle('collapsed');
        }

        function togglePubDesc(el) {
            el.classList.toggle('show-desc');
        }
"""
