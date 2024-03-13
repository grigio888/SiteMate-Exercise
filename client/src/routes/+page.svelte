<script>
    import './style.css';

    export let data;

    import Card from './Card.svelte';

    $: issues = data.issues || [];
    
    const resetStatus = () => {
        issues = issues.filter(issue => issue.id !== undefined);
    }

    const addNew = () => {
        resetStatus();
        issues = [{ editing: true }, ...issues];
    }

    const handleSave = async (e) => {
        let info = e.detail;
        if (info.id === undefined) {
            let resp = await fetch('http://localhost:8000/issues', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(info)
            })
            resp = await resp.json()
            resetStatus();
            issues = [resp.data, ...issues];
        } else {
            let resp =  await fetch(`http://localhost:8000/issues/${info.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(info)
            })
            resp = await resp.json()
            issues = issues.map(issue => {
                if (issue.id === info.id) {
                    return resp.data;
                }
                return issue;
            });
        }
    }

    const handleDelete = async (e) => {
        let info = e.detail;

        if (!confirm('Are you sure you want to delete this issue?')) {
            return;
        }

        let resp = await fetch(`http://localhost:8000/issues/${info.id}`, {
            method: 'DELETE'
        })
        resp = await resp.json()
        issues = issues.filter(issue => issue.id !== info.id);
    }
</script>

<main>
    <h1>Issues Tracker</h1>

    <div class="options">
        <button on:click={addNew}>Add Issue</button>
    </div>

    <div class="issues">
        {#if issues.length === 0}
            <p>No issues found</p>
        {:else}
            {#each issues as issue (issue.id)}
                <Card
                    editing={issue.editing ? true : false}
                    id={issue.id} title={issue.title} description={issue.description}
                    on:save={handleSave}
                    on:delete={handleDelete}
                />
            {/each}
        {/if}
    </div>
</main>

<style>
    main {
        padding: 1em;
    }

    .issues {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1em;
    }

    .options {
        margin-bottom: 1em;
    }
</style>