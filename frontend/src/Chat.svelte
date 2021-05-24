<script>
        let cats = [
		{ id: 'J---aiyznGQ', name: 'Keyboard Cat' },
		{ id: 'z_AbfPXTKms', name: 'Maru' },
		{ id: 'OUtn3pvWmpg', name: 'Henri The Existential Cat' }
	];
</script>

    <body>
        <header>The chatbox will be on the second page since I'll explain and keep track of my work on the first page</header>
        
        <ul>
            {#each cats as { id, name }, i}
                <li><a target="_blank" href="https://www.youtube.com/watch?v={id}">
                    {i + 1}: {name}
                </a></li>
            {/each}
        </ul>
        
        <!-- {% for message in text%}
            <h1>{{message}}</h1>
        {% endfor %} -->

        <form action='http://127.0.0.1:8080/receive' method='GET'>
            <label for="help">How can I help you?</label>
            <input type="text" id="help" value="Enter your question here" name='whatever'>
            <input type="submit" placeholder="send">
        </form>

        <p>It was long and hard but finally the basic chat is here.</p>

        <nav>
            <a href="/">Back to the first page</a>
        </nav>
    </body>
