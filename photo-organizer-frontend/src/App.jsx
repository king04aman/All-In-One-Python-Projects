import { useEffect, useMemo, useState } from 'react';
import { loadLibrary, saveLibrary } from './lib/storage';
import Uploader from './components/Uploader';
import PhotoCard from './components/PhotoCard';
import './styles.css';

function App() {
  const [photos, setPhotos] = useState([]);
  const [q, setQ] = useState('');
  const [tag, setTag] = useState('');

  // load once
  useEffect(() => {
    setPhotos(loadLibrary());
  }, []);

  // persist on change
  useEffect(() => {
    saveLibrary(photos);
  }, [photos]);

  const tags = useMemo(
    () => Array.from(new Set(photos.flatMap((p) => p.tags || []))).sort(),
    [photos]
  );

  const filtered = useMemo(() => {
    let out = photos;
    if (q.trim()) {
      const needle = q.toLowerCase();
      out = out.filter((p) =>
        (p.name + ' ' + (p.location || '') + ' ' + (p.tags || []).join(' '))
          .toLowerCase()
          .includes(needle)
      );
    }
    if (tag) out = out.filter((p) => (p.tags || []).includes(tag));
    // newest first by dateTaken
    return [...out].sort(
      (a, b) => new Date(b.dateTaken) - new Date(a.dateTaken)
    );
  }, [photos, q, tag]);

  function addPhotos(items) {
    setPhotos((prev) => [...items, ...prev]);
  }
  function removePhoto(id) {
    setPhotos((prev) => prev.filter((p) => p.id !== id));
  }
  function updatePhoto(id, patch) {
    setPhotos((prev) =>
      prev.map((p) => (p.id === id ? { ...p, ...patch } : p))
    );
  }

  return (
    <div className="page">
      <div className="container">
        <h1>Photo Organizer</h1>

        <Uploader onAdd={addPhotos} />

        <section className="filters">
          <input
            placeholder="Search…"
            value={q}
            onChange={(e) => setQ(e.target.value)}
          />
          <select value={tag} onChange={(e) => setTag(e.target.value)}>
            <option value="">All tags</option>
            {tags.map((t) => (
              <option key={t} value={t}>
                #{t}
              </option>
            ))}
          </select>
          <button onClick={() => { setQ(''); setTag(''); }}>Reset</button>
        </section>

        {filtered.length === 0 ? (
          <p className="muted">No photos yet or no match.</p>
        ) : (
          <div className="grid">
            {filtered.map((p) => (
              <PhotoCard
                key={p.id}
                photo={p}
                onRemove={removePhoto}
                onUpdate={updatePhoto}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
