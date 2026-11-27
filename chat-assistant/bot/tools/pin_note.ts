import { prompt } from "@grok/agent-sdk";
import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";

type PinnedNote = {
  key: string;
  text: string;
};

export default defineTool({
  description: prompt`
    Pin a short note for this session so you can recall it later in the turn.
    Use when the user asks you to remember a preference, name, or fact.
    Do not pin secrets or credentials.
  `,
  execution: "server",
  effect: "idempotent",
  inputSchema: z.object({
    key: z
      .string()
      .min(1)
      .max(64)
      .describe("Short slug for the note, e.g. preferred-name"),
    text: z.string().min(1).max(500).describe("The note to remember"),
  }),
  async execute({ key, text }, ctx) {
    const storageKey = `note:${ctx.session.id}:${key}`;
    const note: PinnedNote = { key, text };
    await ctx.host.kv.put(storageKey, note);
    return { pinned: true, key, text };
  },
});