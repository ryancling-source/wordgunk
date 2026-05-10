export default async function handler(req, res) {
  const limit = req.query.limit || 50;
  const offset = req.query.offset || 0;

  const response = await fetch(
    `${process.env.SUPABASE_URL}/rest/v1/words?select=*&order=created_at.desc&limit=${limit}&offset=${offset}`,
    {
      headers: {
        'apikey': process.env.SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${process.env.SUPABASE_ANON_KEY}`
      }
    }
  );

  const data = await response.json();
  if (!response.ok) return res.status(500).json({ error: data });
  return res.status(200).json(data);
}


