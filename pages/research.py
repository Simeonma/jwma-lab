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
            text-align: left;
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
                    <img src="images/research/research3.jpg" alt="Integrated photonic chips" loading="lazy" class="research-img">
                    <div class="research-content">
                        <h4 id="item1-title-en">Photonic integrated circuits</h4>
                        <h4 id="item1-title-cn" style="display: none;">集成光子芯片</h4>
                        <p id="item1-desc-en">The rapid growth of AI workloads is pushing electronic chips toward fundamental limits in interconnect bandwidth and energy efficiency. We engineer photonic integrated circuits (PICs) on silicon, silicon nitride, III-V, and thin-film lithium niobate platforms, aiming to process optical information directly on chip. Our research targets high-bandwidth optical interconnects, optical signal processing, and photonic computing architectures that could relieve the bandwidth and energy bottlenecks of AI hardware.</p>
                        <p id="item1-desc-cn" style="display: none;">AI 算力需求的快速增长正将电子芯片推向互连带宽与能效的物理极限。我们基于硅、氮化硅、III-V 族半导体与薄膜铌酸锂等平台研发光子集成芯片（PIC），目标是在芯片上直接以光处理光信息，面向高带宽光互连、光信号处理与光子计算架构，为缓解 AI 硬件的带宽与能耗瓶颈提供新路径。</p>
                    </div>
                </div>

                <div class="research-item hover-card">
                    <img src="images/publications/Room-temperature continuous-wave Dirac-vortex topological lasers on silicon.png" alt="Photonic-crystal lasers" loading="lazy" class="research-img">
                    <div class="research-content">
                        <h4 id="item2-title-en">Photonic-crystal surface-emitting lasers</h4>
                        <h4 id="item2-title-cn" style="display: none;">光子晶体激光器</h4>
                        <p id="item2-desc-en">Semiconductor lasers are everywhere, yet their beam quality and power are ultimately set by the cavity. We design photonic-crystal surface-emitting lasers (PCSELs)—including topological cavity designs—to achieve single-mode operation, narrow linewidth, and high power in a compact, wafer-scale format, targeting LiDAR, coherent optical communications, and precision metrology.</p>
                        <p id="item2-desc-cn" style="display: none;">半导体激光器无处不在，但光束质量与输出功率最终由谐振腔决定。我们设计光子晶体面发射激光器（PCSEL），包括拓扑谐振腔方案，在紧凑的晶圆级尺度上同时实现单模运转、窄线宽与高功率输出，面向激光雷达、相干光通信与精密计量。</p>
                    </div>
                </div>

                <div class="research-item hover-card">
                    <img src="images/research/research5.png" alt="Quantum light-matter hybrids" loading="lazy" class="research-img">
                    <div class="research-content">
                        <h4 id="item3-title-en">Strong light-matter coupling and macroscopic quantum states</h4>
                        <h4 id="item3-title-cn" style="display: none;">强光-物质耦合与宏观量子物态</h4>
                        <p id="item3-desc-en">When light and matter couple strongly enough, they no longer behave as separate entities: exciton-polaritons—half-light, half-matter quasiparticles—form and can condense into macroscopic quantum states. We study this physics in van der Waals materials (TMDs, moiré superlattices, magnetic materials) and engineered photonic lattices, aiming to realize and control polariton Bose–Einstein condensation, quantum fluids, vortices, and supersolids, ideally at room temperature. Beyond fundamental many-body physics, these hybrid states may enable new coherent light sources and quantum simulators.</p>
                        <p id="item3-desc-cn" style="display: none;">当光与物质耦合足够强，二者不再各自独立：激子极化激元——半光半物质的准粒子——得以形成并凝聚为宏观量子态。我们在范德华材料（过渡金属硫族化合物、莫尔超晶格、低维磁性材料）与人工光子晶格中研究这一物理，致力于实现并操控极化激元的玻色-爱因斯坦凝聚、量子流体、涡旋乃至超固体，并探索室温实现。除多体物理本身，这些光-物质混合态有望催生新型相干光源与量子模拟平台。</p>
                    </div>
                </div>

                <div class="research-item hover-card">
                    <img src="images/research/research4.jpg" alt="Nano-electro-mechanical chips" loading="lazy" class="research-img">
                    <div class="research-content">
                        <h4 id="item4-title-en">Nano-electro-mechanical chips</h4>
                        <h4 id="item4-title-cn" style="display: none;">纳米机电芯片</h4>
                        <p id="item4-desc-en">Nanoscale mechanical motion couples naturally to light, electricity, and heat. We design nano-electromechanical systems (NEMS) with engineered—including topologically protected—vibrational modes, aiming at ultra-high frequencies and robust operation, with routes toward RF signal processing, ultrasensitive sensing, and quantum phononics.</p>
                        <p id="item4-desc-cn" style="display: none;">纳米尺度的机械运动天然与光、电、热相互耦合。我们设计具有工程化乃至拓扑保护振动模式的纳米机电系统（NEMS），追求超高频率与高鲁棒性的机械振荡，为射频信号处理、超灵敏传感与量子声子学开辟路径。</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

SCRIPT = ""
