import reflex as rx
from .models import ThemeConfig, Profile, Education, Certification, Skill, Company, Project
from sqlmodel import select, SQLModel

def _ensure_tables():
    """Create all tables if they don't exist yet (safe on repeated calls)."""
    try:
        import sqlalchemy as sa
        from rxconfig import config as app_config
        engine = sa.create_engine(app_config.db_url)
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(f"[seed] Table creation warning: {e}")

def seed_db():
    _ensure_tables()
    with rx.session() as session:
        # If DB already has data, ensure gmail_url is populated and stop further seeding.
        existing_prof = session.exec(select(Profile)).first()
        if existing_prof:
            if not existing_prof.gmail_url:
                existing_prof.gmail_url = "kirthikraj555@gmail.com"
                session.add(existing_prof)
                session.commit()
            return
            
        print("Seeding database...")
        
        # 1. Config
        config = ThemeConfig(
            name="default",
            font_family="Inter, sans-serif",
            base_font_size="16px",
            light_bg="#F5F7F5",
            light_accent="#3ECF8E",
            light_text="#2B3A31",
            light_card_bg="rgba(255, 255, 255, 0.65)",
            dark_bg="#0F1712",
            dark_accent="#53E8A4",
            dark_text="#E8F1EC",
            dark_card_bg="rgba(25, 33, 28, 0.4)"
        )
        session.add(config)
        
        # 2. Profile
        prof = Profile(
            name="Kirthik Raj",
            linkedin_url="https://www.linkedin.com/in/kirthik-raj-93952674",
            gmail_url="kirthikraj555@gmail.com",
            objective_title="Objective / Overview",
            objective_text="Results-driven technology architect known for simplifying development lifecycles through structured thinking, delivering optimized solutions and maintaining consistent client relationships.",
            professional_summary_title="Professional Summary",
            professional_summary_text="""Architect with 11+ years of experience in BPM, integration, and low-code platforms including Appian, IBM BPM IID, JBoss Fuse, UiPath, and OutSystems. 
Brings 7.5+ years of deep Appian expertise with 8 end-to-end Appian deliveries and 3 additional BPM platform projects.
Has led cross-functional teams of up to 23 members across the full project lifecycle, delivering complex enterprise solutions at leading organizations such as Citibank, BNP Paribas etc.
Experienced across Banking, Financial Services, Insurance, Healthcare, Telecom, Automobile and Logistics.
Equally comfortable in Agile and Waterfall environments with a consistent track record of daily stakeholder engagement.""",
            technical_summary_title="Technical Experience Summary",
            technical_summary_text="""Appian BPM Development — Scalable process model design aligned with Appian and SOA best practices. Modular application architecture leveraging Data Fabric and synchronized records.
API design with OAuth 2.0, JWT, and SAML (including self-signed certificate configuration) using SOAP, REST and intergrations utilizing FTP, and SAP BAPI.
Database Design — Version-managed, scalable schema design for high-performance enterprise applications.
UI/UX Development — Responsive, accessible interfaces built to UI/UX best practices within the Appian low-code ecosystem.
AI & Intelligent Automation — Hands-on with Appian Process HQ, AI Skills, and AI Agents for intelligent, data fabric-driven process automation.
Integration Platforms — Enterprise delivery across IBM BPM IID, JBoss Fuse, UiPath (RPA), and OutSystems.
Team Leadership — Cross-functional team leadership (3–23 members); focused on on-time delivery, quality standards, and team development."""
        )
        session.add(prof)
        
        # 3. Education
        session.add(Education(year="2015", examination="B. TECH Information Technology", board_university="R.M.K Engineering college/Anna University", order_index=1))
        session.add(Education(year="2011", examination="12th grade", board_university="Nazareth Matriculation Higher Secondary School", order_index=2))
        session.add(Education(year="2009", examination="10th grade", board_university="Nazareth Matriculation Higher Secondary School", order_index=3))
        
        # 4. Certifications
        session.add(Certification(name="Lead Appian Developer – Level 3", credential_info="https://community.appian.com/members/kirthikrajk0001", order_index=1))
        session.add(Certification(name="Associate Google cloud Engineer", credential_info="Credential ID 2592954d20424b1282e452ff430cdeea", order_index=2))
        session.add(Certification(name="UiPath diploma certification (expired)", credential_info="", order_index=3))
        
        # 5. Skills
        languages = ["tamil", "english"]
        for i, l in enumerate(languages):
            session.add(Skill(category="language", name=l, order_index=i))
            
        techs = ["Appian 18 to 25.4", "IBM BPM IID", "JBOSS Fuse", "python", "html", "css", "sql", "java", "llm and diffusion model tools like vllm, llama.cpp, comfy ui, ollama", "basic understanding on agentic frameworks"]
        for i, t in enumerate(techs):
            session.add(Skill(category="technical", name=t, order_index=i))
            
        # 6. Companies & Projects
        c1 = Company(name="Horizon industries ltd", duration="Latest", roles_and_responsibilities="As an architect 5 members team, my role is to coordinate with product owner in backlog refinement, user stories creation, to sprint retrospection making sure team is aligned to proposed designs and requirements.\nApart from prior Appian handon experience this role involved in extensive stakeholder interactions with canadian clients and refining requirements from Discovery sessions.\nAdditional care was taken to make sure appian latest features like process hq, ai skills and ai agents were utilized to automate triage and document review processes", order_index=1)
        session.add(c1)
        session.commit()
        session.refresh(c1)
        session.add(Project(company_id=c1.id, name="GH", customer="Leading Insurance provider(canada)", technology_used="Appian (25.4), cloud maria db.", description="This software suit is built on Appian to automate insurance document classification, extraction and review to kick start onboarding of new customer on to the insurance platform.", order_index=1))
        
        c2 = Company(name="WNS Vuram", duration="Apr 2025 – Sep 2025", roles_and_responsibilities="As a team leader of 5 members, my role is to coordinate with product owner in backlog refinement, user stories creation, to sprint retrospection making sure team is aligned to proposed designs and requirements.\nApart from prior Appian handon experience this role involved in extensive stakeholder interactions with uae clients and in resolving impedements in requirements along with BA and architects\nAdditional care was taken in db entity design to make sure of scalabilty due to the volume of transactions at the client banks and other services.", order_index=2)
        session.add(c2)
        session.commit()
        session.refresh(c2)
        session.add(Project(company_id=c2.id, name="FAB", customer="Leading Banking client(UAE)", technology_used="Appian (25.2), cloud maria db.", description="This software suit is built on Appian to help banks and importers to handle the contractual agreements (LC & LG) and payment processing in an autonomous way, provided the required details are present in shared documents. Additional support for human in the loop the handle the documents in-case of any missing details or discrepancies.", order_index=1))
        session.add(Project(company_id=c2.id, name="MFS", customer="Leading Assest Management client(tokyo)", technology_used="Appian (25.X), cloud maria db.", description="This software suit is built on Appian to automate the internal meeting schedule according to business rule configurations. It also helps investor managers to organize and track their work items along with meeting memos and communcation logs.", order_index=2))
        
        c3 = Company(name="Xebia", duration="Mar2023 – Sep2024", roles_and_responsibilities="As a team leader of 5 to 23 members, my role is to coordinate with product owner in backlog refinement, user stories creation, to sprint retrospection making sure team is aligned to proposed designs and requirements.\nApart from prior Appian handon experience this role involved in extensive stakeholder interactions from UK, africa, america and Saudi Arabia to design and propose new solution and enterprise level integrations using mq etc.\nAlso performed code reviews inline with appian health check reports and optimized or refactored appian apps with latest features.", order_index=3)
        session.add(c3)
        session.commit()
        session.refresh(c3)
        session.add(Project(company_id=c3.id, name="OPM", customer="Leading medical client(UK)", technology_used="Appian (22.x - 23.3), cloud maria db.", description="OPM is a software suit built on Appian to help clinician and customers who outsource the panel management to collaborate in a single platform. It has various modules to handle functionalities like report generation, case management, interactive configuration management, dynamic form configuration, onboarding module for clinician, customers etc.", order_index=1))
        session.add(Project(company_id=c3.id, name="Order processing system", customer="Leading service provider(Africa)", technology_used="Appian (22.x - 23.3), cloud maria db.", description="OPS is a software suit built on Appian to help our business partners to connect the end users or the customers with various professionals like plumbers, electricians etc. Our system is built to support entire life cycle of a shop management( from registering the service details to maintaining professional information) and that of the order management( from placing the order – coordinating with payment registry – providing feedback and closing the order). This project utilizes both portals and sites as lots of features are built for un registered users.", order_index=2))
        session.add(Project(company_id=c3.id, name="Price Deviation management", customer="Leading Logistics provider(US)", technology_used="Appian (24.1), cloud maria db. And oracle db", description="PDR is a software suit built on Appian to help our business partners to enable their employees to raise or request a reduction in price for the contracts that are signed with their partners, Thus enabling them to provide special offers to their partners and help them to secure the business. This project involves in intense data calculations which utilizes lots of preconfigured formulas to decide whether offer prices can be approved within allowed business standards. It also utilizes appian ui and process to configure these rules and to support life cycle of the request management( from raising a new request to it’s approval stage , escalation stage, till it’s completion and reporting).", order_index=3))
        session.add(Project(company_id=c3.id, name="RA", customer="Aiport from riyadh", technology_used="Appian (24.x), cloud maria db. And oracle db", description="This aiport project handles terminals, bays staff's daily routine checklist configurations by automating daily report generations, alerts and enabling collaboration between various internal teams and external partners via API's", order_index=4))


        c4 = Company(name="Citi India pvt ltd", duration="Nov 2021–Mar 2023", roles_and_responsibilities="As a team leader of 3 members, my role is to coordinate with product owner in backlog refinement, user stories creation, to sprint retrospection\nApart from prior Appian handon experience this role involved in automation proposals and devliery to reduce case configuration time and migration of legacy system data.\nAlso performed code reviews inline with appian health check reports and utilized post deployment process to trigger test rules in dev ops.", order_index=4)
        session.add(c4)
        session.commit()
        session.refresh(c4)
        session.add(Project(company_id=c4.id, name="Workflow builder", customer="citi's own product", technology_used="Appian (21.x –22.x), oracle sql server", description="This appian framework supports depth configurable items for building process models and ui components to accelerate new application development process.", order_index=1))
        session.add(Project(company_id=c4.id, name="Citi Orchestrator Framework", customer="citi's own product", technology_used="Appian (21.x – 22.x), oracle sql server.", description="COF is a highly modular appian framework which orchestrates data flow between various systems like .net, java using web api and integrations. Entire design is modular and asynchronous which makes handling failure and retires simple and flexible", order_index=2))
        session.add(Project(company_id=c4.id, name="Appian Automations For identity provider Migration", customer="citi's own product", technology_used="Appian (21.x – 22.x), oracle sql server.", description="This project involved in building various automated processes to migrate the data from an old ldap based idp to a new java based system which handles the data level elements in an identity management system in greater detail.", order_index=3))

        c5 = Company(name="BNP Paribas India pvt ltd", duration="Feb 2020– Nov 2021", roles_and_responsibilities="As a team leader of 5 members , my role is to coordinate with product owner in backlog refinement, user stories creation, to sprint retrospection\nWorked on multiple Database frameworks (Views and Stored Procedures, triggers)\nDemonstrated proficiency in generating PDFs, Word documents, Excel spreadsheets using Appian smart services and in code reviews with appian best practices.\nExtensive hands-on expertise in Appian, proficient in Sail, Process, Record, Reports, Web APIs, Integration", order_index=5)
        session.add(c5)
        session.commit()
        session.refresh(c5)
        session.add(Project(company_id=c5.id, name="Enterprise Content Management", customer="Leading international bank", technology_used="Appian (18.x – 20.x), oracle sql server", description="ECM is an appian based case management framework used to create different types of cases via in-build configurations and manage life cycle of the case.", order_index=1))

        c6 = Company(name="Tech Mahindra pvt ltd", duration="July 2015 – Jan 2020", roles_and_responsibilities="Functioned as both team member and team leader of 3 members pod. my role involves in making sure the feasibility of requirements with project leader, scrum master and timely delivery of products from backlog.\nDemonstrated proficiency in integrating different systems like mainframe, sap, java api, soap end points etc via IBM/jboss connectors.\nProposed and developed POCs to migrate legacy apps to cloud tools like appian, outsystems and uipath.", order_index=6)
        session.add(c6)
        session.commit()
        session.refresh(c6)
        session.add(Project(company_id=c6.id, name="NNA Middleware", customer="Leading automobile manufacturer (north america)", technology_used="IBM BP IID, JBOSS Fuse, Ui Path, oracle, mysql, DB2, shell scripting, svn, bms, service now, appian (POCs).", description="NNA uses different platforms like mainframe, ibm bpm, jboss fuse and technology stacks like .net and java. Middleware acts as a bus between all these different products and enables logging, data transformation and data transfer.", order_index=1))

        session.commit()
        print("Database seeding completed.")
