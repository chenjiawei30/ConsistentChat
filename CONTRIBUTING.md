# Contributing to Multi-turn Dialogue Generator

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/multi-turn-dialogue-generator.git
   cd multi-turn-dialogue-generator
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .[dev]  # Install development dependencies
   ```

## 🧪 Testing

Before submitting any changes, please ensure all tests pass:

```bash
python test.py
```

## 📝 Code Style

We follow Python best practices:

- **PEP 8** style guidelines
- **Type hints** for function parameters and return values
- **Docstrings** for all public functions and classes
- **Meaningful variable names**

### Code Formatting

We use `black` for code formatting:

```bash
black .
```

### Linting

We use `flake8` for linting:

```bash
flake8 .
```

## 🔧 Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and test them thoroughly

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** on GitHub

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] All tests pass (`python test.py`)
- [ ] Code follows style guidelines
- [ ] Documentation is updated if needed
- [ ] Changes are tested with different configurations

### PR Description

Please include:

- **Summary** of changes
- **Motivation** for the changes
- **Testing** performed
- **Screenshots** if applicable

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment details**:
   - Python version
   - Operating system
   - Package versions

2. **Steps to reproduce**:
   - Clear, numbered steps
   - Expected vs actual behavior

3. **Error messages** and logs

4. **Minimal example** if possible

## ✨ Feature Requests

For new features, please:

1. **Check existing issues** to avoid duplicates
2. **Describe the feature** clearly
3. **Explain the use case** and benefits
4. **Consider implementation** complexity

## 📚 Documentation

- **Code comments** should explain "why", not "what"
- **README updates** for new features
- **Example usage** for complex features
- **API documentation** for new functions

## 🏷️ Release Process

Releases are managed by maintainers:

1. **Version bump** in `setup.py`
2. **Changelog update**
3. **Git tag** creation
4. **GitHub release** with notes

## 🤝 Community Guidelines

- **Be respectful** and inclusive
- **Help others** learn and grow
- **Provide constructive feedback**
- **Follow the code of conduct**

## 📞 Getting Help

- **GitHub Issues** for bugs and feature requests
- **Discussions** for questions and ideas
- **Pull Requests** for code contributions

## 🎯 Areas for Contribution

- **New flow types** for dialogue generation
- **Additional prompt templates**
- **Performance optimizations**
- **Error handling improvements**
- **Documentation enhancements**
- **Test coverage expansion**

Thank you for contributing! 🎉




