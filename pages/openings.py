TITLE = {"en": "Openings - MacroPhotonic Lab", "cn": "招聘信息 - MacroPhotonic Lab"}
NAV_ACTIVE = "openings"

CSS = """
        .intro-text {
            font-size: 17px;
            color: #475569;
            margin-bottom: 40px;
            line-height: 1.8;
            background: #F9FBFF;
            padding: 24px;
            border-radius: 12px;
        }

        .opening-section {
            margin-bottom: 64px;
        }

        .section-subtitle {
            margin-bottom: 32px;
            padding-left: 12px;
        }

        .positions-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 28px;
            width: 100%;
        }

        .position-card {
            background: #ffffff;
            border: 1px solid #F1F5F9;
            border-radius: 12px;
            padding: 32px;
        }

        .position-name {
            font-size: 20px;
            font-weight: 600;
            color: #1E3A8A;
            margin-bottom: 16px;
            text-align: center;
        }

        .position-desc {
            font-size: 16px;
            color: #475569;
            line-height: 1.8;
        }

        .position-desc strong {
            color: #1E3A8A;
        }

        .application-info {
            background: #F9FBFF;
            border-radius: 12px;
            padding: 24px;
            border: 1px solid #E2E8F0;
            margin-top: 40px;
        }

        .application-info h4 {
            font-size: 18px;
            color: #1E3A8A;
            margin-bottom: 16px;
            font-weight: 600;
        }

        .application-info p {
            font-size: 16px;
            color: #475569;
            line-height: 1.8;
        }

        .contact-email {
            color: #3B82F6;
            font-weight: 600;
            text-decoration: none;
        }

        .contact-email:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .page-title { font-size: 24px; }
            .section-subtitle { font-size: 22px; }
            .positions-grid { grid-template-columns: 1fr; gap: 24px; }
            .position-card { padding: 24px; }
            .intro-text { padding: 20px; font-size: 16px; }
            .application-info { padding: 20px; }
        }

        @media (max-width: 600px) {
            .position-name { font-size: 18px; }
            .position-desc { font-size: 15px; }
            .application-info p { font-size: 15px; }
        }

        @media (max-width: 375px) {
            .position-card { padding: 20px; }
            .section-subtitle { font-size: 20px; }
        }
"""

BODY = """
    <div class="container">
        <div class="card">
            <h3 class="page-title" id="about-title-en">About Us</h3>
            <h3 class="page-title" id="about-title-cn" style="display: none;">关于我们</h3>

            <div class="intro-text" id="intro-en">
                We believe the essence of research is pure exploration and creation, and we hope to bring together people who genuinely enjoy exploring the unknown. We are committed to maintaining an equal, inclusive, and mutually supportive team environment, <strong>where everyone can unleash creativity in an open and free atmosphere and eventually grow into an independent and competent researcher</strong>. If you are interested in our research, feel free to contact the PI directly at <a href="mailto:majw@sustech.edu.cn" class="contact-email">majw@sustech.edu.cn</a>. You will typically receive a reply within 3 business days.
            </div>
            <div class="intro-text" id="intro-cn" style="display: none;">
                我们相信科研的本质是纯粹的探索与创造，因此我们希望聚拢一些真正享受探索未知的乐趣的人。我们致力于维持一个平等包容互助的团队环境，<strong>让大家在开放自由的氛围中释放创造力，最终成长为独当一面的科研工作者</strong>。如果你对我们的研究感兴趣，欢迎直接联系PI: <a href="mailto:majw@sustech.edu.cn" class="contact-email">majw@sustech.edu.cn</a>，你一般会在3 个工作日内收到回复。
            </div>

            <h3 class="page-title" id="positions-title-en">Open Positions</h3>
            <h3 class="page-title" id="positions-title-cn" style="display: none;">职位开放</h3>

            <div class="opening-section">
                <div class="positions-grid">

                <div class="position-card hover-card">
                        <div class="position-name" id="postdoc-name-en">Postdoctoral Fellow</div>
                        <div class="position-name" id="postdoc-name-cn" style="display: none;">博士后研究员</div>

                        <div class="position-desc" id="postdoc-desc-en">
                            We currently have 2-3 openings for postdoctoral fellows in the areas of integrated photonic chips, ultrafast optics, and metamaterials.<br><br>
                            <strong>Collaboration Philosophy</strong>:<br>
                            We'll work together to develop research topics that fit your background, give you the resources you need, and push the field forward. We support grant applications, conference attendance, and career development.<br><br>
                            <strong>Basic Requirements</strong>:<br>
                            • Ph.D. degree from a renowned university or research institution at home or abroad<br>
                            • Applicants must have first-author publications in related research areas, demonstrating the capability and potential to conduct high-quality research.<br><br>
                            <strong>Salaries, Benefits & Support</strong>:<br>
                            • Annual salary: <strong>330,000–500,000 RMB</strong> (including Guangdong Province and Shenzhen in-post postdoctoral living subsidies)<br>
                            • Eligible postdocs may apply for subsidies totaling up to <strong>1,000,000 RMB</strong> (not concurrently with the Guangdong and Shenzhen in-post living subsidies)<br>
                            • Postdocs may apply for Shenzhen public rental housing through the university; those not using public rental housing are eligible for a housing subsidy of 2,800 RMB/month (pre-tax) for two years<br>
                            • Academic exchange: in addition to domestic and international exchange opportunities provided by the group, the university offers 25,000 RMB in academic exchange funding over two years<br>
                            • Career development: postdocs who stay in Shenzhen for research work after completing their postdoc term and sign a labor (employment) contract of 3 years or more with a local enterprise or institution may apply for the Shenzhen postdoc research grant for staying in/coming to Shenzhen, receiving 100,000 RMB per year for up to 3 years (subject to the latest Shenzhen application requirements). Outstanding postdocs have the opportunity to be promoted to Research Assistant Professor or Assistant Researcher upon completion
                        </div>
                        <div class="position-desc" id="postdoc-desc-cn" style="display: none;">
                            现招聘博士后研究员 2-3 名，研究方向包括集成光子芯片、超快光学、超材料等。<br><br>
                            <strong>合作理念</strong><br>
                            PI会根据博士后的研究背景共同商量课题，提供充足的实验资源和前沿创新的研究思路。PI将支持其申请基金、参加国际会议，并为未来职业发展提供指导和推荐。<br><br>
                            <strong>基本要求</strong><br>
                            • 获得国内外知名高校或科研机构博士学位<br>
                            • 在相关研究领域以第一作者发表过学术论文，具备开展高质量科研工作的能力和潜力<br><br>
                            <strong>薪资福利与支持</strong><br>
                            • 年薪 <strong>33–50 万元人民币</strong>（含广东省及深圳市在站博士后生活补贴）<br>
                            • 符合条件的博士后可申请享受总计高达 <strong>100 万元</strong>的补贴（与广东省及深圳市在站博士后生活补贴不同时享受）<br>
                            • 可依托学校申请深圳市公租房；未使用公租房的可享受两年税前 2800 元/月的住房补贴<br>
                            • 除课题组提供的国内外学术交流机会外，学校提供两年共计 2.5 万元的学术交流经费<br>
                            • 出站留深从事科研工作并与本市企事业单位签订 3 年以上劳动（聘用）合同的，可申请深圳市博士后留深来深科研资助，每年 10 万元，共资助 3 年（以深圳市最新申报要求为准）；结题后表现优秀者有机会晋升为研究助理教授/助理研究员。
                        </div>
                    </div>

                    <div class="position-card hover-card">
                        <div class="position-name" id="phd-name-en">Ph.D. Student</div>
                        <div class="position-name" id="phd-name-cn" style="display: none;">博士研究生</div>

                        <div class="position-desc" id="phd-desc-en">
                            We are looking for Ph.D. students genuinely interested in research, with a touch of idealism — those who enjoy truly understanding a problem for its own sake, rather than chasing short-term results. For admissions details, please refer to the <a href="https://gs.sustech.edu.cn/#/admission/index">University Admissions Website</a>.<br><br>
                            <strong>Mentoring Philosophy</strong>:<br>
                            New members get hands-on training from senior lab members and the PI, then gradually move into independent projects. You pick your research direction based on what interests you. We'll work together on research ideas and guidance, exploring scientific frontiers and publishing high-impact results.<br><br>
                            <strong>Basic Requirements</strong>:<br>
                            • Master's degree in optoelectronics, electronic engineering, physics, or related disciplines (outstanding bachelor's graduates may apply for direct Ph.D. admission, subject to relevant policies).<br>
                            • Strong academic background (GPA ≥ 85/100 or 3.5/4.0) from top-tier universities.<br><br>
                            <strong>Preferred Expertise</strong>:<br>
                            • Photonic chip design and numerical simulation<br>
                            • Theoretical modeling in solid-state physics and related areas<br>
                            • Experience with free-space optical setup<br>
                            • Experience with device nanofabrication<br>
                            • Proficiency in AI-assisted programming, with experience in building multi-agent systems
                        </div>
                        <div class="position-desc" id="phd-desc-cn" style="display: none;">
                            我们希望招收真正对科研感兴趣、带一点理想主义的博士研究生——享受把一个问题真正弄懂的过程，而不只是追逐短期的成果。招生详情请参考<a href="https://gs.sustech.edu.cn/#/admission/index">学校官网</a>。<br><br>
                            <strong>培养理念</strong><br>
                            新人会由PI或有经验的高年级学生指导基础训练，逐步过渡到独立项目；学生可根据个人兴趣和特长选择研究方向，PI会提供可行的科研想法和技术指导，共同探索科学前沿、发表高水平成果。<br><br>
                            <strong>基本要求</strong><br>
                            • 光电信息工程、电子工程、物理学或相关专业硕士学位（优秀本科生可依据相关政策申请直博）<br>
                            • 顶尖高校毕业，具备优秀的学术背景（GPA ≥ 85/100 或 3.5/4.0）<br><br>
                            <strong>优先考虑的专长</strong><br>
                            • 光子芯片的设计及数值模拟<br>
                            • 固体物理及相关物理方向的理论建模<br>
                            • 具备空间光学光路搭建经验<br>
                            • 具备器件纳米加工经验<br>
                            • 熟练运用 AI 辅助编程工具进行开发，具备多智能体（multi-agent）系统搭建经验
                        </div>
                    </div>

                    <div class="position-card hover-card">
                        <div class="position-name" id="master-name-en">Master Student</div>
                        <div class="position-name" id="master-name-cn" style="display: none;">硕士研究生</div>

                        <div class="position-desc" id="master-desc-en">
                            We always welcome motivated students with genuine curiosity in photonics and physics. For details, please refer to the <a href="https://gs.sustech.edu.cn/#/admission/index">University Admissions Website</a>.<br><br>
                            <strong>Mentoring Philosophy</strong>:<br>
                            New members get hands-on training from senior lab members and the PI, then gradually move into independent projects. You pick your research direction based on what interests you. We'll work together on research ideas and guidance, exploring scientific frontiers and publishing high-impact results.<br><br>
                            <strong>Basic Requirements</strong>:<br>
                            • Bachelor's degree in optoelectronics, electronic engineering, physics, or related disciplines.<br>
                            • Strong academic background (GPA ≥ 85/100 or 3.5/4.0) from top-tier universities.<br><br>
                            <strong>Preferred Expertise</strong>:<br>
                            • Device nanofabrication / material synthesis<br>
                            • Device design / numerical simulations / theoretical modeling<br>
                            • Chip / fiber / free-space optoelectronic characterization<br>
                            • Artificial intelligence algorithms / programming
                        </div>
                        <div class="position-desc" id="master-desc-cn" style="display: none;">
                            我们持续招收对光子学的工程和物理有浓厚兴趣的硕士研究生。详情请参考<a href="https://gs.sustech.edu.cn/#/admission/index">学校官网</a>。<br><br>
                            <strong>培养理念</strong><br>
                            新人会由PI或有经验的高年级学生指导基础训练，逐步过渡到独立项目；学生可根据个人兴趣和特长选择研究方向，PI会提供可行的科研想法和技术指导，共同探索科学前沿、发表高水平成果。<br><br>
                            <strong>基本要求</strong><br>
                            • 光电信息工程、电子工程、物理学或相关专业本科学历<br>
                            • 顶尖高校毕业，具备优秀的学术背景（GPA ≥ 85/100 或 3.5/4.0）<br><br>
                            <strong>优先考虑的专长</strong><br>
                            • 器件纳米加工 / 材料制备<br>
                            • 器件设计 / 数值模拟 / 理论建模<br>
                            • 光子芯片 / 光纤光学 / 自由空间光学表征<br>
                            • 人工智能算法 / 编程开发
                        </div>
                    </div>

                    <div class="position-card hover-card">
                        <div class="position-name" id="ra-name-en">Research Assistant</div>
                        <div class="position-name" id="ra-name-cn" style="display: none;">研究助理</div>

                        <div class="position-desc" id="ra-desc-en">
                            If you are interested in hands-on research experience in photonics and nanotechnology, or wish to gain a deeper understanding of our research group, feel free to contact us!<br><br>
                            • Flexible start date to accommodate your schedule<br>
                            • Personalized short-term projects and one-on-one guidance<br>
                            • Competitive stipend
                        </div>
                        <div class="position-desc" id="ra-desc-cn" style="display: none;">
                            如果您对光子芯片和纳米技术领域的一线科研经验感兴趣，或者想要对我们课题组进行深入了解，欢迎联系我们！我们将会提供:<br>
                            • 个性化的短期课题和一对一指导<br>
                            • 灵活的入职时间，可根据个人安排调整<br>
                            • 具有竞争力的待遇
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </div>
"""

SCRIPT = ""
