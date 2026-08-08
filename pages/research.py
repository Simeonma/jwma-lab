TITLE = {"en": "Research - MacroPhotonic Lab", "cn": "研究方向 - MacroPhotonic Lab"}
NAV_ACTIVE = "research"

CSS = """
        .research-container {
            display: grid;
            grid-template-columns: 1fr;
            gap: 28px;
            width: 100%;
        }

        .research-item {
            margin-bottom: 0;
            display: flex;
            flex-direction: row;
            align-items: flex-start;
            height: 100%;
            padding: 24px;
            border: 1px solid #F1F5F9;
            border-radius: 12px;
        }

        .research-content {
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        .research-img {
            width: 40%;
            height: auto;
            max-height: 240px;
            object-fit: cover;
            border-radius: 12px;
            margin-right: 28px;
            margin-bottom: 0;
            flex-shrink: 0;
        }

        .research-item h4 {
            font-size: 20px;
            color: #1E3A8A;
            margin-bottom: 8px;
            text-align: center;
        }

        .research-item p {
            font-size: 16px;
            line-height: 1.9;
            color: #1F2937;
            flex-grow: 1;
            margin-top: 0;
        }

        @media (max-width: 768px) {
            .card h3 { font-size: 24px; }
            .research-container {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            .research-item {
                flex-direction: column;
                padding: 16px;
            }
            .research-img {
                width: 100%;
                height: 220px;
                margin-right: 0;
                margin-bottom: 16px;
            }
            .research-item h4 { font-size: 22px; margin-bottom: 8px; }
            .research-item p { font-size: 16px; }
        }

        @media (max-width: 480px) {
            .research-img { height: 180px; }
        }
"""

BODY = """
    <div class="container">
        <div class="card">
            <h3 id="research-title-en">Research Interests</h3>
            <h3 id="research-title-cn" style="display: none;">研究兴趣</h3>

            <div class="research-container">
                <div class="research-item hover-card">
                    <img src="images/research/research3.jpg" alt="Integrated photonic chips" class="research-img">
                    <div class="research-content">
                        <h4 id="item1-title-en">Photonic integrated circuits</h4>
                        <h4 id="item1-title-cn" style="display: none;">集成光子芯片</h4>
                        <p id="item1-desc-en">We build photonic integrated circuits (PICs) on various platforms — silicon photonics, silicon nitride, III-V semiconductors, thin-film lithium niobate. Our goal: high-performance, scalable, and energy-efficient solutions for optical information processing, high-bandwidth interconnects, and photonic computing.</p>
                        <p id="item1-desc-cn" style="display: none;">我们围绕硅光子学、氮化硅、III-V半导体和薄膜铌酸锂等前沿材料平台，研发高性能先进光子集成芯片，聚焦为下一代光信息处理、高带宽光互连及光子计算领域，打造高性能、可扩展、低能耗的核心解决方案。</p>
                    </div>
                </div>

                <div class="research-item hover-card">
                    <img src="images/publications/Room-temperature continuous-wave Dirac-vortex topological lasers on silicon.png" alt="Photonic-crystal lasers" class="research-img">
                    <div class="research-content">
                        <h4 id="item2-title-en">Photonic-crystal surface-emitting lasers</h4>
                        <h4 id="item2-title-cn" style="display: none;">光子晶体激光器</h4>
                        <p id="item2-desc-en">We design and make next-gen photonic-crystal lasers (PCSELs) that are super stable, narrow-band, and high-power — perfect for LiDAR, optical communications, and precision measurements.</p>
                        <p id="item2-desc-cn" style="display: none;">我们专注于下一代光子晶体面发射激光器的设计、纳米制备与综合表征，致力于在稳定单模工作、超窄线宽、衍射极限光束质量与高功率输出方面实现性能突破，面向车载激光雷达、长距离相干光通信、高精度计量等应用。</p>
                    </div>
                </div>

                <div class="research-item hover-card">
                    <img src="images/research/research5.png" alt="Quantum light-matter hybrids" class="research-img">
                    <div class="research-content">
                        <h4 id="item3-title-en">Quantum materials and light-matter interaction</h4>
                        <h4 id="item3-title-cn" style="display: none;">量子材料及光-物质相互作用物理</h4>
                        <p id="item3-desc-en">We study strong light-matter interactions in van der Waals materials — TMDs, moiré superlattices, magnetic materials. We look for interesting quantum phases and collective effects, and explore their applications in on-chip optoelectronics and quantum photonics.</p>
                        <p id="item3-desc-cn" style="display: none;">我们研究新型范德华材料体系（包括过渡金属硫族化合物、莫尔超晶格与低维磁性材料）中的强光-物质相互作用，在该体系中实现新奇的宏观量子相与相干集体激发，并探索其在高性能片上光电器件与量子光子芯片中的应用。</p>
                    </div>
                </div>

                <div class="research-item hover-card">
                    <img src="images/research/research4.jpg" alt="Nano-electro-mechanical chips" class="research-img">
                    <div class="research-content">
                        <h4 id="item4-title-en">Nano-electro-mechanical chips</h4>
                        <h4 id="item4-title-cn" style="display: none;">纳米机电芯片</h4>
                        <p id="item4-desc-en">We make nano-electro-mechanical systems (NEMS) with special topological properties, hitting ultra-high frequencies and excellent reliability. This opens up new possibilities for RF signal processing, sensing, and quantum phononics.</p>
                        <p id="item4-desc-cn" style="display: none;">我们开发具备拓扑非平庸特性的先进纳米机电系统（NEMS），聚焦实现高鲁棒性与超高频率的器件性能，为下一代射频（RF）信号处理、超灵敏传感与量子声子学领域提供新方案。</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

SCRIPT = ""
