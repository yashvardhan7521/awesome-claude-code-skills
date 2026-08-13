<p align="center">
  <img src="assets/header.svg" alt="Awesome Claude Skills" width="100%">
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://github.com/anthropics/skills"><img src="https://img.shields.io/badge/Agent%20Skills-Anthropic-141413?style=flat-square" alt="Anthropic Agent Skills"></a>
  <a href="https://docs.anthropic.com/"><img src="https://img.shields.io/badge/Claude-Code-d97757?style=flat-square" alt="Claude Code"></a>
  <a href="https://developers.openai.com/codex/use-cases"><img src="https://img.shields.io/badge/Codex-compatible-6a9bcc?style=flat-square" alt="Codex"></a>
</p>

Awesome Claude Skills

A curated, human-maintained directory of high-value Skills, plugins, and agent tooling for Claude, Claude Code, Codex, Gemini CLI, Cursor, and other Agent Skills-compatible environments.

Skills are small, reusable instruction packages that give an AI agent specialized workflows, knowledge, scripts, references, and assets. The format is increasingly portable across coding agents, so this list favors projects that are useful beyond a single vendor where practical.

📖 About

Awesome Claude Code Skills is a community-driven repository that helps developers discover, compare, and learn the best Claude Code skills.

Instead of scrolling through scattered repositories and documentation, you'll find everything in one place with consistent ratings, categories, installation guides, and practical use cases.

Why this list exists

The ecosystem is growing faster than anyone should reasonably be expected to track. There are excellent skills everywhere, alongside a heroic amount of duplicated, abandoned, or barely tested markdown.

This list aims to be the useful bit.

Curation standard

A project is favored when it has:

Real utility for a recurring workflow.

Active maintenance and a credible maintainer or organization.

Good implementation quality, not just a flashy README.

Portability across agents when the skill format supports it.

Clear installation and licensing information.

Evidence of adoption, testing, or professional use where available.

Safety note: Third-party plugins can contain code, MCP servers, hooks, or other executable components. Read the source and review permissions before installing anything you do not trust.

Official Skills

Anthropic maintains the reference implementation of Agent Skills and publishes a set of production-oriented and example skills. Its repository currently includes document-generation skills for PDF, DOCX, PPTX, and XLSX, plus creative and technical skills such as Canvas Design, Web Application Testing, MCP Builder, and Skill Creator.

📄 Document Skills

PDF — Create, edit, extract, and analyze PDF documents using a structured workflow.

DOCX — Create and modify professional Word documents with controlled formatting and reusable document workflows.

PPTX — Build and edit PowerPoint presentations with structured slide-generation and editing workflows.

XLSX — Create and analyze Excel workbooks with formulas, formatting, and spreadsheet-specific reasoning.

🎨 Design & Creative

Canvas Design — Create original visual artwork and static designs as PNG or PDF artifacts.

Algorithmic Art — Generate original p5.js-based algorithmic and generative art with seeded randomness and interactive parameters.

Theme Factory — Apply curated typography and color systems consistently across decks, documents, reports, and web artifacts.

Brand Guidelines — Apply Anthropic's official visual identity, colors, typography, and presentation styling to artifacts.

🧑‍💻 Development

Web Application Testing — Test local web applications with Playwright, including UI behavior, browser logs, screenshots, and debugging.

MCP Builder — Guide the design, implementation, and evaluation of high-quality MCP servers for external services.

Skill Creator — Create, improve, evaluate, and benchmark Skills so they trigger reliably and perform well.

Frontend Design — Build distinctive, production-grade frontend interfaces instead of generic AI-looking pages.

🧩 Official Plugin & Reference Hubs

Anthropic Agent Skills — The main Anthropic repository containing the reference skill implementations, Agent Skills specification, templates, and examples.

Claude Code Plugins Official — Anthropic's managed directory of high-quality Claude Code plugins, including internal plugins and vetted external plugins.

Claude Code Plugin Development — Official skills and tooling for building, reviewing, and packaging Claude Code plugins.

Community Skills

Community projects are where the ecosystem gets interesting, because people inevitably automate the oddly specific workflows that official documentation politely ignores.

🧑‍💻 Development & Engineering

Superpowers — A mature agentic development framework combining skills for TDD, debugging, planning, code review, worktrees, and multi-agent workflows across Claude Code, Codex, Cursor, Gemini CLI, and other agents.

Trail of Bits Skills — Security-focused skills for vulnerability research, smart-contract auditing, testing, and defensive engineering with Claude Code and Codex support.

Trail of Bits Curated Skills — A security-conscious marketplace of Claude Code plugins that have been reviewed and approved by Trail of Bits.

Frontend Design — A cross-agent frontend-design skill for Claude Code, Codex, and Gemini CLI that provides explicit aesthetic systems for building polished interfaces.

📚 Research, Knowledge & Context

Skill Seekers — Turn documentation sites, GitHub repositories, PDFs, videos, notebooks, and other sources into structured AI-ready Skills and knowledge assets.

Notion Skills — Store, collaborate on, publish, and synchronize Agent Skills from a shared Notion database across Claude, Codex, Cursor, Gemini, and other agents.

Notion Claude Code Plugin — An official Notion plugin bundling Notion Skills, the Notion MCP server, and useful Claude Code commands into one installable package.

📣 Business, Marketing & Growth

Marketing Skills — A focused collection of CRO, copywriting, SEO, analytics, and growth-engineering Skills for Claude Code and other agents.

Developer GTM Claude Skills — A broad cross-agent collection spanning developer GTM, SEO, writing, Notion, product design, coding, and job-search workflows.

📊 Data & Analysis

Data Analysis Skill — Turn CSV and Excel data into polished analysis with multi-expert reasoning, interactive HTML reports, charts, and presentation-ready outputs.

🗂️ Discovery & Curated Collections

Awesome Claude Skills by Composio — A large, categorized catalog of practical Skills and plugins covering documents, development, data, marketing, writing, creativity, productivity, security, and automation.

Awesome Claude Code — A broader hand-picked directory of Claude Code skills, plugins, developer tooling, resources, and workflow patterns.

⭐ Cross-Agent Picks

These are especially worth checking when you want one Skill or repository to travel with you instead of rebuilding the same thing for every AI coding agent.

Project

Claude Code

Codex

Other agents

Best for

Superpowers

✅

✅

✅

Software engineering workflows

Skill Seekers

✅

✅

✅

Turning external knowledge into Skills

Trail of Bits Skills

✅

✅

—

Security and auditing

Notion Skills

✅

✅

✅

Team skill management

Frontend Design

✅

✅

✅

High-quality UI design

Marketing Skills

✅

✅

✅

Marketing and growth

🧩 Plugins

Community and third-party plugins worth knowing about. Support labels below reflect the information provided with this list; where support was not verified in the supplied material, it is marked Not verified rather than pretending the robot knows everything.

<table>
  <thead>
    <tr>
      <th>Plugin</th>
      <th>Claude Code</th>
      <th>Codex</th>
      <th>Other agents</th>
      <th>Specific feature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>OmniRoute</strong></td>
      <td>✅ Yes</td>
      <td>Not verified</td>
      <td>200+ AI providers via its routing layer</td>
      <td>Routes Claude Code usage across free AI providers and automatically switches to another model when a usage limit is reached.</td>
    </tr>
    <tr>
      <td><strong>Claude Mem</strong></td>
      <td>✅ Yes</td>
      <td>Not verified</td>
      <td>Not verified</td>
      <td>Persistent project/session memory that summarizes work and makes information recallable across sessions.</td>
    </tr>
    <tr>
      <td><strong>Headroom</strong></td>
      <td>✅ Yes</td>
      <td>Not verified</td>
      <td>Model-agnostic compression proxy</td>
      <td>Compresses context before it reaches the model so less token-heavy, unnecessary context is passed through.</td>
    </tr>
    <tr>
      <td><strong>Claude Code Setup</strong></td>
      <td>✅ Yes</td>
      <td>Not verified</td>
      <td>Claude Code plugin ecosystem</td>
      <td>Scans a codebase and recommends useful hooks, Skills, subagents, and MCP servers, while helping remove unnecessary setup.</td>
    </tr>
    <tr>
      <td><strong>Task Observer</strong></td>
      <td>⚠️ Not verified</td>
      <td>Not verified</td>
      <td>Not verified</td>
      <td>Claimed to observe working patterns and continuously improve other Skills in the background.</td>
    </tr>
  </tbody>
</table>

📐 Agent Skills Standard & Documentation

Agent Skills Specification — The open specification describing the portable SKILL.md format and supporting conventions.

Agent Skills — The public home for the open Agent Skills standard.

Anthropic Skills Documentation — Anthropic's user-facing explanation of what Skills are and how they work.

Claude Code Plugins Documentation — Official documentation for installing and developing Claude Code plugins.

OpenAI Codex Skills & Use Cases — Current OpenAI guidance showing how Codex uses Skills for repeatable workflows.

🤝 Contributing

A good contribution is more valuable than a large contribution.

Suggest a new skill

Open an issue using the repository's skill suggestion template, or submit a pull request that adds the Skill to the appropriate category.

Include the project URL, the exact Skill or plugin name, and a one-sentence description.

Note which agents it supports, such as Claude Code, Codex, Gemini CLI, Cursor, or other Agent Skills-compatible tools.

Include the license and any important installation or dependency requirements.

Prefer projects that are maintained, useful, clearly documented, and safe to inspect.

Do not submit duplicates, abandoned projects, obvious spam, or repositories whose value is mainly a giant uncurated list of links.

Pull request checklist

Link works and points to the canonical project or Skill.

Name and description are accurate.

Skill is placed in the right category.

Project has a visible license or clearly documented usage terms.

Repository is reasonably maintained.

Any required API keys, MCP servers, hooks, or external services are documented.

The contribution adds real value rather than duplicating an existing entry.

🧭 Curation philosophy

This list is intentionally small enough to trust and large enough to be useful.

A higher star count does not automatically mean a better Skill. We care more about whether a Skill is maintained, understandable, portable, safe to inspect, and genuinely useful in real work.

The ecosystem will keep changing. That is precisely why this README should be curated rather than blindly generated.

Disclaimer

This is an independent community list and is not affiliated with or endorsed by Anthropic, OpenAI, Google, Microsoft, Cursor, or any project listed here.

Always review third-party repositories before installing Skills, plugins, hooks, MCP servers, or other executable components.

🤝 Contributing

Contributions are welcome.

If you'd like to add a new skill or improve an existing one, please read the contribution guidelines in CONTRIBUTING.md before opening a pull request.

📄 License

This project is licensed under the MIT License.

⭐ If you find this repository useful, consider giving it a star to support the project.
