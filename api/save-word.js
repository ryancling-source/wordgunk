export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { word, pos, pronunciation, etymology, definition, example, category, human_coined } = req.body;

  const response = await fetch(`${process.env.SUPABASE_URL}/rest/v1/words`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'apikey': process.env.SUPABASE_ANON_KEY,
      'Authorization': `Bearer ${process.env.SUPABASE_ANON_KEY}`,
      'Prefer': 'return=representation'
    },
    body: JSON.stringify({ word, pos, pronunciation, etymology, definition, example, category, human_coined: human_coined ?? false })
  });

  const data = await response.json();
  if (!response.ok) return res.status(500).json({ error: data });
  return res.status(200).json({ success: true, id: data[0]?.id });
}


