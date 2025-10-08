import { useRef, useState } from 'react';
import { fileToDataURL, parseTags } from '../lib/utils';
import { makeId } from '../lib/storage';


export default function Uploader({ onAdd }) {
const [defaults, setDefaults] = useState({ location: '', tags: '' });
const inputRef = useRef(null);


async function handleFiles(files) {
if (!files || !files.length) return;
const items = [];
for (const f of files) {
const src = await fileToDataURL(f);
items.push({
id: makeId(),
name: f.name,
src,
ext: (f.name.split('.').pop() || '').toLowerCase(),
dateTaken: new Date(f.lastModified || Date.now()).toISOString(),
location: defaults.location.trim(),
tags: parseTags(defaults.tags),
uploadedAt: new Date().toISOString(),
});
}
onAdd(items);
if (inputRef.current) inputRef.current.value = '';
}


return (
<section className="card">
<h2>Upload</h2>
<input
ref={inputRef}
type="file"
accept="image/*"
multiple
onChange={e => handleFiles(e.target.files)}
/>
<div className="row" style={{ marginTop: 8 }}>
<input
placeholder="Default location"
value={defaults.location}
onChange={e => setDefaults(d => ({ ...d, location: e.target.value }))}
/>
<input
placeholder="Default tags (comma-separated)"
value={defaults.tags}
onChange={e => setDefaults(d => ({ ...d, tags: e.target.value }))}
/>
</div>
<button style={{ marginTop: 8 }} onClick={() => handleFiles(inputRef.current?.files)}>
Add Selected
</button>
</section>
);
}