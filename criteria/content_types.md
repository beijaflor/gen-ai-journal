# Content Type Classification Guide

## Purpose

This document defines 9 objective content types for systematic article classification during curation. Each type receives specific editorial treatment to optimize reader experience and journal composition.

## Classification Principles

- **Objective**: Based on content structure and format, not subjective value judgments
- **Mutually Exclusive**: Each article belongs to exactly one type
- **Treatment-Oriented**: Each type implies specific summary approach and editorial voice

---

## The 9 Content Types

### **News & Announcements**

**What it is**: Official communications about product releases, company announcements, and version updates.

**Key Characteristics**:
- Published by official sources (companies, organizations, maintainers)
- Factual reporting of events, launches, or updates
- Time-sensitive information
- Formal announcement tone

**Examples**:
- GitHub Copilot new feature announcement
- OpenAI API pricing changes
- React 19 release notes

**Editorial Treatment**: Concise factual summary with business impact analysis

---

### **Research & Analysis**

**What it is**: Data-driven studies, comparative analysis, and systematic technical research.

**Key Characteristics**:
- Contains empirical data, measurements, or systematic comparison
- Methodology-driven approach
- Evidence-based conclusions
- Academic or rigorous analytical style

**Examples**:
- LLM performance benchmarks
- Code completion tool effectiveness studies
- **Current example**: AI Hype discourse analysis (hidde.blog)

**Editorial Treatment**: Technical depth with methodology review and practical implications

---

### **Tutorial & Guide**

**What it is**: Step-by-step instructions and educational how-to content.

**Key Characteristics**:
- Sequential, actionable instructions
- Learning-oriented structure
- Code examples or implementation details
- "How to" or "Getting started" format

**Examples**:
- "Setting up GitHub Copilot in VS Code"
- "Building an AI assistant with OpenAI API"
- "Implementing RAG architecture"

**Editorial Treatment**: Practical value assessment with complexity and prerequisite evaluation

---

### **Opinion & Commentary**

**What it is**: Personal perspectives, editorial viewpoints, and thought pieces.

**Key Characteristics**:
- Author's personal stance or interpretation
- Subjective analysis or argumentation
- Editorial or blog post format
- Opinion-driven conclusions

**Examples**:
- Developer productivity philosophy posts
- Future of programming predictions
- **Current example**: AI output etiquette perspective (distantprovince.by)

**Editorial Treatment**: Perspective analysis with contrarian considerations and practical relevance

---

### **Technical Reference**

**What it is**: Documentation, specifications, and architectural reference material.

**Key Characteristics**:
- Reference-oriented content
- Technical specifications or standards
- API documentation or code patterns
- Implementation-focused details

**Examples**:
- API documentation updates
- Architectural pattern explanations
- Code style guides

**Editorial Treatment**: Technical accuracy verification with adoption guidance

---

### **Industry Report**

**What it is**: Market analysis, trend reports, and survey-based insights.

**Key Characteristics**:
- Statistical data and market research
- Survey results or industry polling
- Business intelligence focus
- Market trend analysis

**Examples**:
- Developer survey results
- AI adoption in enterprise reports
- Programming language popularity statistics

**Editorial Treatment**: Signal extraction with startup ecosystem implications

---

### **Tools**

**What it is**: Software tools, libraries, frameworks, and development utilities.

**Key Characteristics**:
- Specific software or utility focus
- Tool reviews, comparisons, or launches
- Implementation or integration guidance
- Feature announcements for development tools

**Examples**:
- New VS Code extension reviews
- CLI tool comparisons
- Framework version updates
- AI coding assistant evaluations

**Editorial Treatment**: Practical evaluation with workflow integration assessment

---

### **AI Hype**

**What it is**: Critical analysis of AI discourse and examination of promotional claims.

**Key Characteristics**:
- Skeptical or critical stance toward AI marketing
- Analysis of industry rhetoric and claims
- Debunking or reality-checking focus
- Meta-commentary on AI discourse

**Examples**:
- **Current example**: AI hype contribution analysis (hidde.blog)
- AI capability overclaim critiques
- Marketing vs. reality examinations

**Editorial Treatment**: Extended critical analysis with contrarian perspective and practical reality check

---

### **AI Etiquette**

**What it is**: Social implications and norms around AI-generated content and human-AI interaction.

**Key Characteristics**:
- Human-AI interaction focus
- Communication design implications
- Social norms and etiquette considerations
- UX and ethical aspects of AI integration

**Examples**:
- **Current example**: AI output sharing etiquette (distantprovince.by)
- Human-AI collaboration best practices
- AI transparency and disclosure norms

**Editorial Treatment**: Design impact analysis with UX considerations and communication guidelines

---

## Decision Framework

### For Ambiguous Cases

1. **Primary Content Focus**: What is the main subject matter?
2. **Author Intent**: What is the primary purpose of the article?
3. **Content Structure**: How is the information presented?
4. **Source Type**: Who published it and in what context?

### Common Edge Cases

- **Tool Tutorial vs. Tutorial**: If focused on specific tool → ⚙️ Tools; if teaching general concepts → 📖 Tutorial
- **Opinion with Data vs. Research**: If personal interpretation dominates → 💭 Opinion; if methodology dominates → 🔬 Research
- **News vs. Analysis**: If announcing facts → 📰 News; if interpreting implications → 🔬 Research

### Classification Priority

1. **Specialized Types** (AI Hype, AI Etiquette, Tools) take precedence when applicable
2. **Content Structure** over author intent
3. **Primary Focus** over secondary elements

---

## Integration with Curation Workflow

### In STEP_04_CURATE_MAIN.md

1. **Review Summary**: Read the article summary
2. **Apply Framework**: Use decision criteria above
3. **Assign Type**: Select single most appropriate type
4. **Document Rationale**: Brief note on classification reasoning
5. **Apply Treatment**: Use type-specific editorial approach

### Quality Assurance

- **Distribution Check**: Avoid clustering all articles in 1-2 types
- **Type Balance**: Aim for diverse type representation
- **Treatment Consistency**: Ensure editorial approach matches assigned type

---

## Editorial Treatment Summary

| Type | Length | Focus | Voice |
|------|--------|-------|-------|
| 📰 News | Brief | Business Impact | Factual |
| 🔬 Research | Extended | Technical Depth | Analytical |
| 📖 Tutorial | Medium | Practical Value | Evaluative |
| 💭 Opinion | Medium | Perspective Analysis | Balanced Critical |
| 🛠️ Technical | Medium | Accuracy & Adoption | Technical |
| 📊 Industry | Brief | Signal Extraction | Strategic |
| ⚙️ Tools | Medium | Workflow Integration | Practical |
| 🎭 AI Hype | Extended | Critical Analysis | Contrarian |
| 🤝 AI Etiquette | Medium | Design Impact | Thoughtful |