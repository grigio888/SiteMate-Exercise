export async function load({ fetch }) {
    let resp = await fetch('http://localhost:8000/issues')
    resp = await resp.json()

    return {
        issues: resp.data || []
    }
}