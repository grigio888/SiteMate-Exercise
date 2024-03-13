<script>
    import { createEventDispatcher } from "svelte";

    let card;
    export let editing = false;

    export let id = undefined;
    export let title = '';
    export let description = '';

    $: isEditing = editing;

    const dispatch = createEventDispatcher();

    const handleCancel = () => {
        isEditing = false;
        if (id === undefined) {
            card.parentNode.removeChild(card)
        }
    }
</script>

<div class="card" bind:this={card}>
    <div style:display={isEditing ? 'flex' : 'none'}>
        <input type="text" bind:value={title} placeholder="Title"/>
        <textarea bind:value={description} placeholder="Description"></textarea>
        <div class="options">
            <button on:click={() => {isEditing = false; dispatch('save', { id, title, description })}}>
                save
            </button>
            <button on:click={handleCancel}>
                cancel
            </button>
        </div>
    </div>
    <div style:display={isEditing ? 'none' : 'block'}>
        <h2>{title}</h2>
        <p>{description}</p>
        <div class="options">
            <button on:click={() => isEditing = true}>
                edit
            </button>
            <button on:click={() => dispatch('delete', { id })}>
                delete
            </button>
        </div>
    </div>
</div>

<style>
    h2 {
        margin: 0;
    }

    .card, .card > div {
        display: flex;
        flex-direction: column;
    }

    .card > div {
        gap: 1em;
        height: max-content;
        border: 1px solid black;
        border-radius: 5px;
        padding: 1em;
    }

    .options {
        display: flex;
        gap: 1em;

        width: 100%;
        display: flex;
        justify-content: space-between;
    }

    .options button {
        width: 100%;
    }
</style>