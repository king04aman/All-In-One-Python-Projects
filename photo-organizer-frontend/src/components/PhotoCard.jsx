import { useState } from 'react';
import { parseTags } from '../lib/utils';


export default function PhotoCard({ photo, onRemove, onUpdate }) {
const [editing, setEditing] = useState(false);
const [draft, setDraft] = useState({
location: photo.location || '',
tags: (photo.tags || []).join(', '),
dateTaken: photo.dateTaken ? photo.dateTaken.slice(0, 16) : '',
});


function save() {
onUpdate(photo.id, {
location: draft.location.trim(),
tags: parseTags(draft.tags),
dateTaken: draft.dateTaken ? new Date(draft.dateTaken).toISOString() : photo.dateTaken,
});
setEditing(false);
}


const pretty = photo.dateTaken ? new Date(photo.dateTaken).toLocaleString() : 'date n/a';


return (
<figure className="card">
<img src={photo.src} alt={photo.name} className="thumb" loading="lazy" />
<figcaption>
<div className="name" title={photo.name}>{photo.name}</div>
{!editing ? (
<>
<div className="meta">{photo.location || '—'} · {pretty}</div>
<div className="tags">
{(photo.tags || []).length ? (
photo.tags.map(t => <span key={t} className="tag">#{t}</span>)
) : (
<span className="muted">no tags</span>
)}
</div>
<div className="actions">
<button onClick={() => setEditing(true)}>Edit</button>
<button className="danger" onClick={() => onRemove(photo.id)}>Delete</button>
</div>
</>
) : (
<>
<input
value={draft.location}
onChange={e => setDraft(d => ({ ...d, location: e.target.value }))}
placeholder="Location"
/>
<input
value={draft.tags}
onChange={e => setDraft(d => ({ ...d, tags: e.target.value }))}
placeholder="Tags, comma-separated"
/>
<input
type="datetime-local"
value={draft.dateTaken}
onChange={e => setDraft(d => ({ ...d, dateTaken: e.target.value }))}
/>
<div className="actions">
<button className="primary" onClick={save}>Save</button>
<button onClick={() => setEditing(false)}>Cancel</button>
</div>
</>
)}
</figcaption>
</figure>
);
}