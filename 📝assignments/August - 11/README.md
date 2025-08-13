# Assignment - August 11

**Goal:**
Make a Library Assistant using the OpenAI Agents SDK.

**It should:**
- Search for books
- Check book availability (only for registered members)
- Give library timings
- Ignore non-library questions

**Must Use:**
- Agent
- Runner.run / Runner.run_sync
- @function_tool
- @input_guardrail
- RunContextWrapper
- dynamic_instruction
- BaseModel
- ModelSettings

**Steps:**
- User Context → Pydantic model with name and member_id.
- Guardrail Agent → Stops non-library queries.
- Input Guardrail Function → Uses guardrail agent.
- Member Check Function → Allows availability tool only if user is valid.

**Function Tools:**
- Search Book Tool → Returns if the book exists.
- Check Availability Tool → Returns how many copies are available.
- Dynamic Instructions → Personalize based on user name.
- Library Agent → Add tools, guardrails, and model settings.
- Book Database → Store book names and copies in a Python dictionary; tools must use this data.
- Multiple Tools Handling → Make sure agent can search and check availability in one query.

**Test with at least 3 queries and print results.**

- **Submit Here:** [https://forms.gle/PaJHC5qMNQE2VjyK9](https://forms.gle/PaJHC5qMNQE2VjyK9)


## Note

- Feel free to complete the assignment in any way you like, using resources from the internet such as youtube videos, articles, etc.
- You can use ChatGPT or any other AI tools to learn the concepts, but you should write the code in your own hands (not copy-paste).
