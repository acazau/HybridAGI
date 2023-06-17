UPDATE_TEXT_TEMPLATE=\
"""
Please Output update the input Text to integrate the following Modifications if relevant.
If no Modifications are relevant, Output the unchanged Text.

Text:
{text}
Modifications:
{modifications}
Output:"""

UPDATE_TEXT_PROMPT = PromptTemplate(
    input_variables = ["text", "modifications"],
    template = UPDATE_TEXT_TEMPLATE
)