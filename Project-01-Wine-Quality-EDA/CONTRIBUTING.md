# Contributing to Wine Quality EDA

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## 📋 How to Contribute

### 1. **Report Issues**
Found a bug or have a suggestion? 
- Open an [Issue](../../issues) with a clear title and description
- Include steps to reproduce (for bugs)
- Mention your environment (Python version, OS)

### 2. **Submit Improvements**
- Fork the repository
- Create a feature branch: `git checkout -b feature/your-feature-name`
- Commit changes: `git commit -m 'Add brief description'`
- Push to branch: `git push origin feature/your-feature-name`
- Open a Pull Request with detailed description

### 3. **Code Standards**
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Use meaningful variable and function names
- Ensure notebooks are cleaned before committing (remove unnecessary cell outputs)

### 4. **Documentation**
- Update README.md if adding new features
- Document new functions with docstrings
- Add examples for new analyses

## 🚀 Development Workflow

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dev dependencies
pip install -r requirements.txt

# 3. Make your changes
# 4. Test your changes
python -m pytest  # if tests exist

# 5. Commit and push
git add .
git commit -m 'Descriptive commit message'
git push origin feature/your-feature-name
```

## 📝 Commit Message Guidelines

- Use clear, descriptive titles
- Reference issues when applicable: `Fixes #123`
- Examples:
  - ✅ Good: `Add bivariate analysis between alcohol and quality`
  - ❌ Bad: `Fixed stuff`

## ✅ Pull Request Checklist

Before submitting a PR, ensure:
- [ ] Code follows PEP 8 standards
- [ ] Notebooks are cleaned (outputs removed where appropriate)
- [ ] Changes are documented
- [ ] Tests pass (if applicable)
- [ ] Commit messages are descriptive
- [ ] No large files added (< 50MB)

## 📞 Contact

For major changes, open an issue first to discuss proposed changes.

---

Thank you for contributing to making this project better! 🙏
