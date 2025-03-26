
INSIGHT_EXTRACTION_PROMPT = '''
<GOAL>
You are tasked with extracting key insights from a meeting transcript. 
An insight is a specific piece of information, fact, or detail expressed in a clear subject-verb-object (SVO) format.
Extract 10-15 key insights from this meeting transcript.
</GOAL>

<GUIDELINES>
1. Each insight should be self-contained and express a single idea or fact
2. Format insights as simple declarative sentences (subject-verb-object)
3. Focus on actionable, specific, and concrete information
4. Capture details from all parts of the transcript, including tables or complex sections
5. Maintain factual accuracy - do not infer beyond what's explicitly stated
</GUIDELINES>

<OUTPUT_FORMAT>
- Generate insights as a pipe-separated list (e.g., "Insight One | Insight Two | Insight Three").
- Each insight should be a concise phrase or short sentence.
- Do not include explanations or additional text.
</OUTPUT_FORMAT>

<EXAMPLE>
"The team agreed to launch Product X by June 15th | Sarah will create the marketing materials by next week | The budget for the project was approved at $50,000 | Customer feedback showed 85% satisfaction with the beta version"
</EXAMPLE>

<CONTEXT>
Meeting Transcript:
{transcript}
</CONTEXT>
'''

CONCEPT_EXTRACTION_PROMPT = '''
<GOAL>
You are tasked with distilling higher-level concepts from a list of document insights.
A concept is a cohesive abstraction that connects related insights, reducing redundancy while preserving essential themes.
</GOAL>

<GUIDELINES>
1. Analyze the insights to identify common themes, topics, or overarching ideas.
2. Group related insights under broader, meaningful concepts.
3. Express each concept as a concise phrase or short sentence.
4. Focus on reducing noise and redundancy while maintaining the document's core themes.
5. Aim for 1-3 concepts per document.
6. Do not include the document name in the concept.
</GUIDELINES>

<OUTPUT_FORMAT>
- Generate concepts as a pipe-separated list (e.g., "Concept One | Concept Two | Concept Three").
- Each concept should be a concise phrase or short sentence.
- Do not include explanations or additional text.
</OUTPUT_FORMAT>

<EXAMPLE>
Insights:
- The company’s revenue grew by 15% last quarter.
- Customer satisfaction scores increased after the new support system was implemented.
- Employee turnover decreased by 10% following the introduction of flexible work hours.
- The new marketing campaign led to a 20% increase in website traffic.

Concepts:
"Workforce Stability Drives Operational Success | Integrated Customer Experience Enhances Revenue | Employee Flexibility Fuels Marketing Impact"
</EXAMPLE>

<CONTEXT>
Insights:
{insights}
</CONTEXT>

Generate concepts that synthesize these insights:
'''

CONCEPT_VALIDATION_PROMPT = '''
<GOAL>
Evaluate the following concepts derived from document insights. Determine if they are acceptable based on the criteria below.
</GOAL>

<GUIDELINES>
1. Concepts should be cohesive and meaningful abstractions.
2. They should synthesize insights into higher-level relationships or themes, not just summarize.
3. Each concept should reveal valuable connections between insights.
4. Reject if concepts are redundant, vague, or fail to connect insights effectively.
</GUIDELINES>

<CONTEXT>
Concepts:
{concepts}

Insights:
{insights}
</CONTEXT>

<OUTPUT_FORMAT>
- Respond with "Accept" if the concepts meet the criteria.
- Respond with "Reject" if they do not, and provide a brief explanation (1-2 sentences).
</OUTPUT_FORMAT>
'''

THEME_EXTRACTION_PROMPT = '''
<GOAL>
You are tasked with identifying overarching themes from meeting concepts.
A theme represents the highest level of abstraction, connecting multiple concepts into strategic or fundamental categories.
</GOAL>

<GUIDELINES>
1. Analyze the concepts to find the most significant patterns or categories
2. Express themes as concise labels or phrases
3. Focus on strategic importance or fundamental categories
4. Aim for 1-3 themes that provide the most valuable high-level view
</GUIDELINES>

<EXAMPLE>
Concepts:
- Product X Launch Timeline and Marketing Plan
- Budget Allocation and Resource Constraints
- Customer Feedback Implementation Strategy

Theme: "Product X Go-to-Market Strategy"
</EXAMPLE>

<CONTEXT>
Concepts:
{concepts}
</CONTEXT>

Generate themes that connect these concepts:
'''

THEME_VALIDATION_PROMPT = '''
<GOAL>
Evaluate whether the provided themes accurately represent high-level abstractions of the given concepts and insights.
</GOAL>

<GUIDELINES>
1. Check if themes connect multiple concepts into strategic or fundamental categories.
2. Ensure themes are concise and informative.
3. Verify that themes provide a valuable high-level view of the concepts.
</GUIDELINES>

<CONTEXT>
Insights:
{insights}

Concepts:
{concepts}

Themes:
{themes}
</CONTEXT>

Respond with "accept" if the themes are satisfactory, or provide feedback on how they can be improved.
'''