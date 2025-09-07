# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-09-04

### Added
- Initial release of Multi-turn Dialogue Generator
- Clean, simplified data structure for dialogue categories and flow definitions
- Two-step generation process: query generation → response generation → merge
- Support for original prompt templates with `{{info_flows_steps}}` parameter
- Robust error handling with retry mechanisms
- Real-time saving with checkpoint continuation
- Comprehensive test suite
- Support for 6 different flow types:
  - `problem_diagnosis_to_solution`
  - `theory_to_scene`
  - `user_needs_to_solution`
  - `concept_to_cross_domain`
  - `single_to_multiple_views`
  - `time_series_analysis`
- 8 pre-defined dialogue categories with multiple scenarios
- Batch generation capabilities
- Single dialogue testing functionality
- MIT License
- Comprehensive documentation and examples

### Features
- **Simplified Data Structure**: Clean JSON format with categories and flow definitions
- **Original Template Compatibility**: Uses existing prompt templates without modification
- **Information Flow Support**: Maintains `{{info_flows_steps}}` parameter support
- **Error Handling**: Robust retry mechanisms and graceful fallbacks
- **Real-time Saving**: Checkpoint continuation support
- **Easy Configuration**: Simple config.py setup
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Python 3.8+**: Modern Python support

### Technical Details
- Built with OpenAI-compatible API client
- Jinja2 templating for dynamic prompt generation
- JSON-based data storage and output
- Modular, object-oriented design
- Type hints throughout codebase
- Comprehensive error handling
- Progress tracking with tqdm

### Documentation
- Complete README with usage examples
- API documentation in code
- Configuration examples
- Contributing guidelines
- MIT License

---

## [Unreleased]

### Changed
- **Removed `num_turns` parameter**: Dialogue turn count is now determined by the prompt template (6-8 turns as specified in `prompt_template_en.txt`)
- **Simplified API**: Removed redundant `num_turns` parameter from all generation methods
- **Updated configuration**: Removed `num_turns` from `GENERATION_CONFIG`

### Planned Features
- Support for additional LLM providers
- Custom flow type definitions
- Web interface for dialogue generation
- Export to different formats (CSV, JSONL, etc.)
- Dialogue quality metrics
- Batch processing optimizations
- Docker containerization
- CI/CD pipeline setup

### Potential Improvements
- Async API support for better performance
- Caching mechanisms for repeated requests
- Dialogue validation and quality checks
- More sophisticated error recovery
- Configuration validation
- Logging improvements
- Performance monitoring
