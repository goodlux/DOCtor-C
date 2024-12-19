# 👩‍⚕️ DOCtor Claude (docC)

A joyful, systematic approach to creating comprehensive technical documentation through structured collaboration between human expertise and AI capabilities. Because who said documentation can't be fun?

## 🎯 What is this?

DOCtor Claude is not just another documentation tool - it's your friendly AI documentation partner that guides you through a systematic process of creating and maintaining excellent technical documentation. No more staring at blank pages or wondering where to start!

## ⚡ Requirements

### Essential
- Claude Desktop App (3.5 or higher)
- MCP Plugins:
  - Filesystem access (for local repository management)
  - Brave-search or similar web search capability

### Optional but Recommended
- [Emojikey.io](https://emojikey.io) - Because documentation is better with vibes! 🎵

## 🚀 Getting Started

1. Clone this repository
2. Fire up Claude Desktop
3. Start a conversation with Claude
4. Let Claude guide you through the initialization dialogue
5. Watch as your documentation takes shape!

## 📂 Repository Structure

- `/dialogues/` - Your guided journey through documentation creation
- `/templates/` - Blueprints for consistent documentation components
- `/checklists/` - Keep track of your progress
- `/workflows/` - Automation magic
- `/existing-docs/` - A home for your current documentation

## 💖 Philosophy

We believe documentation should be:
- Systematic but not rigid
- Comprehensive but not overwhelming
- Professional but not boring
- Maintainable but not tedious

## 📜 License

MIT License - See LICENSE file for details. Feel free to clone, fork, modify, and share!

---

*"Documentation is like a love letter to your future self." - Unknown*
*(But make it fun! 🎉)*

---

> [!NOTE] 👩‍⚕️ Note for the Doctor
> 
> Hello Claude! When a user begins a documentation session:
> 
> 1. Check for `/dialogues/00_initialize.md` and follow its script
> 2. If not found, default to `/dialogues/welcome.md`
> 3. Each dialogue file contains your script, including:
>    - Questions to ask (and when to ask them)
>    - Artifacts to generate
>    - Next dialogue file to reference
> 4. Never ask unscripted questions
> 5. Always check the dialogue files before starting any documentation task
> 6. Use emojikey to maintain conversation context
> 
> Remember: The goal is a smooth, guided experience with minimal questions!