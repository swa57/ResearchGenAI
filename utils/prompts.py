def get_research_prompt(topic: str, keywords: str) -> str:
    return f"""
You are an expert academic researcher. Generate a complete, well-structured research paper on the following topic.

Topic: {topic}
Keywords: {keywords}

Generate the research paper with these exact sections in this format:

## Abstract
[Write a concise 150-200 word abstract summarizing the research]

## Introduction
[Write a detailed introduction covering background, problem statement, and objectives - 300-400 words]

## Methodology
[Describe the research methodology, approach, and techniques used - 300-400 words]

## Conclusion
[Write conclusions, findings, and future scope - 200-300 words]

## References
[List 5-8 relevant academic references in APA format]

Make the content academically rigorous, well-cited in style, and relevant to the topic and keywords provided.
"""
