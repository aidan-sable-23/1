import { defineEval } from "@grok/agent-sdk/evals";

export default defineEval({
  tags: ["smoke"],
  description: "Pins a session note when asked to remember something.",
  async test(t) {
    await t.send(
      'Please remember that my preferred name is Ada. Use the pin_note tool with key "preferred-name".',
    );
    t.succeeded();
    t.calledTool("pin_note", {
      input: { key: "preferred-name" },
    });
  },
});
