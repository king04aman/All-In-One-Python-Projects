const STORAGE_KEY = 'photo_organizer_v1';

export function loadLibrary() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {            // ← no unused var
    return [];
  }
}

export function saveLibrary(photos) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(photos));
  } catch {            // ← no unused var
    // ignore quota errors for demo
  }
}

export function makeId() {
  return Date.now().toString(36) + Math.random().toString(36).slice(2);
}