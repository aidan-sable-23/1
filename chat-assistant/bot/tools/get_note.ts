import { prompt } from "@grok/agent-sdk";
import { defineTool } from "@grok/agent-sdk/tools";
import * as z from "zod/v4";

export default defineTool({
  description: prompt`
    Read a note previously pinned for this session with pin_note.
    Call when the user asks what you remembered, or before answering
    from a pinned preference.
  `,
  execution: "server",
  effect: "read",
  inputSchema: z.object({
    key: z.string().min(1).max(64).describe("Slug used when the note was pinned"),
  }),
  async execute({ key }, ctx) {
    const storageKey = `note:${ctx.session.id}:${key}`;
    const note = await ctx.host.kv.get(storageKey);
    if (note === undefined) {
      return { found: false as const, key };
    }
    return { found: true as const, note };
  },
});
