TITLE = {"en": "Members - MacroPhotonic Lab", "cn": "团队成员 - MacroPhotonic Lab"}
NAV_ACTIVE = "people"

CSS = """
        .section-title {
            font-size: 28px;
            color: #1E3A8A;
            margin-bottom: 16px;
            padding-bottom: 16px;
            border-bottom: 2px solid #E2E8F0;
            font-weight: 700;
            text-align: left;
            position: relative;
        }

        .pi-card {
            display: flex;
            gap: 24px;
            align-items: center;
            margin-bottom: 48px;
            padding-bottom: 24px;
            border-bottom: 1px solid #E2E8F0;
        }

        .pi-avatar {
            width: 240px;
            height: 240px;
            border-radius: 50%;
            overflow: hidden;
            background: #F8FAFC;
            flex-shrink: 0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }

        .pi-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            background-color: #F8FAFC;
        }

        .pi-info h4 {
            font-size: 24px;
            color: #1E3A8A;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .pi-info .position {
            font-size: 18px;
            color: #4B5563;
            margin-bottom: 16px;
            font-weight: 500;
        }

        .pi-info .bio {
            font-size: 16px;
            line-height: 1.8;
            margin-bottom: 16px;
            color: #1F2937;
            text-align: left;
        }

        .pi-info .cv-link {
            display: inline-block;
            margin-right: 12px;
            padding: 7px 18px;
            border: 1.5px solid #1E3A8A;
            border-radius: 8px;
            color: #1E3A8A;
            font-weight: 600;
            font-size: 15px;
            text-decoration: none;
            transition: background 0.2s, color 0.2s;
        }

        .pi-info .cv-link:hover {
            background-color: #1E3A8A;
            color: #ffffff;
        }

        .members-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 28px;
            margin-top: 10px;
            width: 100%;
        }

        .member-card {
            text-align: center;
            background: #ffffff;
            border: 1px solid #F1F5F9;
            border-radius: 12px;
            padding: 20px 16px;
        }

        .member-avatar {
            width: 196px;
            height: 196px;
            border-radius: 50%;
            overflow: hidden;
            background: #F8FAFC;
            margin: 0 auto 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }

        .member-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            background-color: #F8FAFC;
        }

        .member-avatar.placeholder {
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            color: #94A3B8;
        }

        .member-info h5 {
            font-size: 18px;
            color: #1E3A8A;
            margin-bottom: 4px;
            font-weight: 600;
        }

        .member-info .member-position {
            font-size: 16px;
            color: #4B5563;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .member-info .research-area {
            font-size: 16px;
            color: #1F2937;
            line-height: 1.6;
            padding: 0 4px;
            text-align: left;
            margin-bottom: 5px;
        }

        .alumni-list {
            margin-top: 4px;
        }

        .alumni-empty {
            padding: 12px 4px;
            font-size: 16px;
            color: #94A3B8;
        }

        .alumni-row {
            display: flex;
            gap: 24px;
            padding: 12px 4px;
            border-bottom: 1px solid #F1F5F9;
            align-items: baseline;
        }

        .alumni-row:last-child {
            border-bottom: none;
        }

        .alumni-name {
            min-width: 160px;
            font-weight: 600;
            color: #1E3A8A;
            flex-shrink: 0;
        }

        .alumni-info {
            font-size: 16px;
            color: #4B5563;
            line-height: 1.6;
        }

        .member-info .contact {
            font-size: 16px;
            color: #1E3A8A;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .member-info .contact::before {
            content: '\U0001f4e7';
            font-size: 16px;
            margin-right: 4px;
        }

        .join-card {
            border: 1px solid #F1F5F9;
        }

        .join-card .member-avatar.placeholder {
            color: #D97706;
        }

        .join-dot {
            display: inline-block;
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background-color: #D97706;
            margin-right: 6px;
            vertical-align: middle;
            animation: badge-pulse 2s ease-in-out infinite;
        }

        .join-link {
            display: inline-block;
            margin-top: 12px;
            padding: 6px 20px;
            background: #1E3A8A;
            color: #ffffff;
            border-radius: 8px;
            text-decoration: none;
            font-size: 15px;
            font-weight: 500;
            transition: all 0.2s;
        }

        .join-link:hover {
            background: #1E40AF;
        }

        @media (max-width: 768px) {
            .section-title { font-size: 24px; }
            .pi-card { flex-direction: column; align-items: center; text-align: center; gap: 20px; }
            .pi-avatar { width: 200px; height: 200px; }
            .pi-info .bio { text-align: center; }
            .members-grid { grid-template-columns: 1fr; gap: 40px; }
        }

        @media (max-width: 600px) {
            .pi-avatar { width: 170px; height: 170px; }
            .member-avatar { width: 150px; height: 150px; }
        }

        @media (max-width: 480px) {
            .pi-avatar { width: 150px; height: 150px; }
        }
"""

BODY = """
    <div class="container">
        <div class="card">
            <h3 class="section-title" id="pi-title-en">Principal Investigator</h3>
            <h3 class="section-title" id="pi-title-cn" style="display: none;">课题组负责人</h3>

            <div class="pi-card">
                <div class="pi-avatar">
                    <img loading="lazy" src="images/members/Dr J Ma.jpg" alt="Jingwen Ma">
                </div>
                <div class="pi-info">
                    <h4 id="pi-name-en">Dr. Jingwen Ma</h4>
                    <h4 id="pi-name-cn" style="display: none;">马静文博士</h4>

                    <div class="position" id="pi-position-en">Associate Professor, Department of Electrical and Electronic Engineering, SUSTech</div>
                    <div class="position" id="pi-position-cn" style="display: none;">南方科技大学电子与电气工程系副教授</div>

                    <div class="bio" id="pi-bio-en">
                        Dr. Jingwen Ma received his Ph.D. degree in Electronic Engineering from The Chinese University of Hong Kong in 2021. He then worked as a Postdoctoral Fellow and Research Assistant Professor in Prof. Xiang Zhang's group at the University of Hong Kong. He is currently an Associate Professor in the Department of Electrical and Electronic Engineering, Southern University of Science and Technology, and a recipient of the National Overseas High-Level Talent Program. His research interests include integrated photonic chips, semiconductor lasers, light-matter interaction physics, and metamaterials.
                    </div>
                    <div id="pi-links-en" style="margin-top: 4px;">
                        <a href="files/cv.pdf" class="cv-link" target="_blank">Full CV</a>
                        <a href="https://www.sustech.edu.cn/en/faculties/jingwenma.html" class="cv-link" target="_blank">Faculty Profile</a>
                    </div>
                    <div class="bio" id="pi-bio-cn" style="display: none;">
                        2021年获得香港中文大学电子工程博士学位，此后在香港大学张翔院士课题组从事博士后研究并任研究助理教授。现任南方科技大学电子与电气工程系副教授，入选国家海外高层次人才计划。研究兴趣包括集成光子芯片、半导体激光器、光-物质相互作用物理、纳米超表面与超材料等。
                    </div>
                    <div id="pi-links-cn" style="display: none; margin-top: 4px;">
                        <a href="files/cv.pdf" class="cv-link" target="_blank">完整简历</a>
                        <a href="https://www.sustech.edu.cn/zh/faculties/jingwenma.html" class="cv-link" target="_blank">学校教师主页</a>
                    </div>
                    </div>
                </div>

            <h3 class="section-title" id="members-title-en">Members</h3>
            <h3 class="section-title" id="members-title-cn" style="display: none;">团队成员</h3>

            <div class="members-grid">
                <div class="member-card hover-card">
                    <div class="member-avatar placeholder">
                        <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    </div>
                    <div class="member-info">
                        <h5 id="xt-name-en">Tianyu Xu</h5>
                        <h5 id="xt-name-cn" style="display: none;">徐天宇</h5>
                        <div class="member-position" id="xt-pos-en">Master's Student</div>
                        <div class="member-position" id="xt-pos-cn" style="display: none;">硕士研究生</div>
                        <div class="research-area" id="xt-bio-en">Tianyu Xu received his bachelor's degree from SUSTech and is currently pursuing a master's degree there. His research interests include intelligent optical systems.</div>
                        <div class="research-area" id="xt-bio-cn" style="display: none;">本科毕业于南方科技大学，现为南方科技大学硕士研究生，研究兴趣为智能光学系统。</div>
                    </div>
                </div>
                <div class="member-card hover-card">
                    <div class="member-avatar">
                        <img loading="lazy" src="images/members/Jiong Ouyang.jpg" alt="Jiong Ouyang">
                    </div>
                    <div class="member-info">
                        <h5 id="oj-name-en">Jiong Ouyang</h5>
                        <h5 id="oj-name-cn" style="display: none;">欧阳炯</h5>
                        <div class="member-position" id="oj-pos-en">Master's Student</div>
                        <div class="member-position" id="oj-pos-cn" style="display: none;">硕士研究生</div>
                        <div class="research-area" id="oj-bio-en">Jiong Ouyang received his bachelor's degree from Shenzhen University and is currently pursuing a master's degree at the Southern University of Science and Technology. His research interests include nanophotonics.</div>
                        <div class="research-area" id="oj-bio-cn" style="display: none;">本科毕业于深圳大学，目前在南方科技大学攻读硕士学位，研究兴趣为纳米光子学。</div>
                    </div>
                </div>
                <div class="member-card hover-card">
                    <div class="member-avatar">
                        <img loading="lazy" src="images/members/Jie Liu.jpg" alt="Jie Liu">
                    </div>
                    <div class="member-info">
                        <h5 id="jl-name-en">Jie Liu</h5>
                        <h5 id="jl-name-cn" style="display: none;">刘杰</h5>
                        <div class="member-position" id="jl-pos-en">Master's Student</div>
                        <div class="member-position" id="jl-pos-cn" style="display: none;">硕士研究生</div>
                        <div class="research-area" id="jl-bio-en">Jie Liu is a master's student at SUSTech. He completed his undergraduate studies at Hunan University of Technology and Business. His research interests include intelligent optical systems.</div>
                        <div class="research-area" id="jl-bio-cn" style="display: none;">南方科技大学在读硕士研究生，本科毕业于湖南工商大学电子信息工程专业，研究兴趣为智能光学系统。</div>
                    </div>
                </div>
                <div class="member-card hover-card">
                    <div class="member-avatar">
                        <img loading="lazy" src="images/members/Han Zhang.jpg" alt="Han Zhang">
                    </div>
                    <div class="member-info">
                        <h5 id="hz-name-en">Han Zhang</h5>
                        <h5 id="hz-name-cn" style="display: none;">张涵</h5>
                        <div class="member-position" id="hz-pos-en">Research Assistant</div>
                        <div class="member-position" id="hz-pos-cn" style="display: none;">研究助理</div>
                        <div class="research-area" id="hz-bio-en">Han Zhang received his bachelor's degree from South China University of Technology and is currently pursuing a master's degree at the National University of Singapore. His research interests include photonic crystal lasers.</div>
                        <div class="research-area" id="hz-bio-cn" style="display: none;">本科毕业于华南理工大学，现于新加坡国立大学攻读硕士学位，研究兴趣为光子晶体激光器。</div>
                    </div>
                </div>
                <div class="member-card hover-card">
                    <div class="member-avatar">
                        <img loading="lazy" src="images/members/Yikang Peng.jpg" alt="Yikang Peng">
                    </div>
                    <div class="member-info">
                        <h5 id="yp-name-en">Yikang Peng</h5>
                        <h5 id="yp-name-cn" style="display: none;">彭怡康</h5>
                        <div class="member-position" id="yp-pos-en">Research Assistant</div>
                        <div class="member-position" id="yp-pos-cn" style="display: none;">研究助理</div>
                        <div class="research-area" id="yp-bio-en">Yikang Peng is about to graduate from Sun Yat-sen University. His research interests include optical computing and photonic chips.</div>
                        <div class="research-area" id="yp-bio-cn" style="display: none;">即将毕业于中山大学，研究兴趣为光计算与光子芯片。</div>
                    </div>
                </div>
                <div class="member-card hover-card">
                    <div class="member-avatar">
                        <img loading="lazy" src="images/members/Yidan Zhu.jpg" alt="Yidan Zhu">
                    </div>
                    <div class="member-info">
                        <h5 id="yz-name-en">Yidan Zhu</h5>
                        <h5 id="yz-name-cn" style="display: none;">朱奕丹</h5>
                        <div class="member-position" id="yz-pos-en">Undergraduate Intern</div>
                        <div class="member-position" id="yz-pos-cn" style="display: none;">本科实习生</div>
                        <div class="research-area" id="yz-bio-en">Yidan Zhu is an undergraduate student at the Department of Electronic and Electrical Engineering, SUSTech. Her research interests include topological photonic crystals.</div>
                        <div class="research-area" id="yz-bio-cn" style="display: none;">南方科技大学电子与电气工程系在读本科生，研究兴趣为拓扑光子晶体。</div>
                    </div>
                </div>
                <div class="member-card hover-card">
                    <div class="member-avatar">
                        <img loading="lazy" src="images/members/Jiaheng Zheng.jpg" alt="Jiaheng Zheng">
                    </div>
                    <div class="member-info">
                        <h5 id="jz-name-en">Jiaheng Zheng</h5>
                        <h5 id="jz-name-cn" style="display: none;">郑家恒</h5>
                        <div class="member-position" id="jz-pos-en">Undergraduate Intern</div>
                        <div class="member-position" id="jz-pos-cn" style="display: none;">本科实习生</div>
                        <div class="research-area" id="jz-bio-en">Jiaheng Zheng is an undergraduate student at the Department of Electronic and Electrical Engineering, SUSTech. His research interests include photonic chips.</div>
                        <div class="research-area" id="jz-bio-cn" style="display: none;">南方科技大学电子与电气工程系在读本科生，研究兴趣为光子芯片。</div>
                    </div>
                </div>
                <div class="member-card join-card hover-card">
                    <div class="member-avatar placeholder">
                        <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    </div>
                    <div class="member-info">
                        <h5 id="join-title-en">Join Our Team</h5>
                        <h5 id="join-title-cn" style="display: none;">加入我们</h5>
                        <div class="member-position" id="join-pos-en"><span class="join-dot"></span>PhD Student · Postdoc · RA</div>
                        <div class="member-position" id="join-pos-cn" style="display: none;"><span class="join-dot"></span>博士生 · 博士后 · 研究助理</div>
                        <a href="openings.html" class="join-link" id="join-link-en">View Openings →</a>
                        <a href="openings.html" class="join-link" id="join-link-cn" style="display: none;">查看职位 →</a>
                    </div>
                </div>
            </div>

            <h3 class="section-title" id="alumni-title-en">Alumni</h3>
            <h3 class="section-title" id="alumni-title-cn" style="display: none;">毕业生去向</h3>

            <div class="alumni-list">
                <div class="alumni-empty" id="alumni-empty-en">To be updated.</div>
                <div class="alumni-empty" id="alumni-empty-cn" style="display: none;">待更新。</div>
                <!-- To add an alumnus, remove the "To be updated" lines above and copy this block:
                <div class="alumni-row">
                    <span class="alumni-name" id="al1-name-en">San Zhang</span>
                    <span class="alumni-name" id="al1-name-cn" style="display: none;">张三</span>
                    <span class="alumni-info" id="al1-info-en">M.S. 2027 &middot; Ph.D. at MIT</span>
                    <span class="alumni-info" id="al1-info-cn" style="display: none;">2027年硕士毕业，现于麻省理工学院攻读博士</span>
                </div>
                -->
            </div>
        </div>
    </div>
"""

SCRIPT = ""
