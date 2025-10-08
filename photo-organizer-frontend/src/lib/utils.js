export function parseTags(input) {
return (input || '')
.split(',')
.map(t => t.trim())
.filter(Boolean);
}


export function fileToDataURL(file) {
return new Promise((resolve, reject) => {
const fr = new FileReader();
fr.onload = () => resolve(fr.result);
fr.onerror = reject;
fr.readAsDataURL(file);
});
}