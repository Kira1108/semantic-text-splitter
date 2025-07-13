PLAN_PROMPT = """
Given a document, you need to generate a plan on how to split it into chunks.

Principles:
1. If the document has section headers, explain how sections look like, the pattern of section headers.
2. Based on the section content, determine the granularity of splitting, for example, split on top-level headers like 1. 2. 3. or 1.1 1.2 ....
3. IF the document does not have section headers, explain how to split it based on the content(Semantical chunking)
3. briefly explain the main content of the document.

Output:
Your output should contain the following parts:
1. split strategy: a brief description of how to split the document, section header patterns, and granularity.
2. document summary: a brief summary of the document content.

Note:
Your output should be less than 300 Chinese characters, So you have to make it brief and concise.

Here is the document you need to plan for chunking
<document>
{document}
</document>
"""


ANCHOR_FINDER_PROMPT = """
Semantically split the following text into smaller chunks by identifying the optimal split points(anchors).

Constraints:
1. when splitting based on the resulting anchors, each chunk should be no between 500 - 1000 Chinese characters.
2. anchors are found according to the splitting plan provided.
3. do not need to add split anchors at the beginning or end of the text.

<splitting-plan>
{plan}
</splitting-plan>

Here is the text you need to semantically split:
<text>
{text}
</text>

You need to return a strcutured json object defined by SemanticSplitAnchors.
NOTE: each anchor sentence should be quoted EXACTLY from the original text, and it should be short enough(LESS THAN 15 Chinese characters is preferred) to be unique, but long enough to be meaningful.
UNIQUE SECTION HEADERS AS ANCHOR TEXTS ARE ALWAYS PREFERRED over other sentences.
"""
