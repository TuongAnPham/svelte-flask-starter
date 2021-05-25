<script>
    import axios from 'axios'
        let messages = [
            'test'
	];

    function getdata() {
        axios.get('http://127.0.0.1:8080/get').then(resp => {

        console.log(resp.data);
        messages=resp.data
        });
    }

    function send() {
        let input = document.getElementById("help")
        console.log(input.value)
    }

    // setInterval(getdata, 1000);
</script>

    <body>
        <header>The chatbox will be on the second page since I'll explain and keep track of my work on the first page</header>
        
        <ul>
            {#each messages as m, i}
                <li>
                    {m}
                </li>
            {/each}
        </ul>

        <!-- {% for message in text%}
            <h1>{{message}}</h1>
        {% endfor %} -->

        <form on:submit|preventDefault={send}>
        <!-- <form action='http://127.0.0.1:8080/receive' method='GET'> -->
            <label for="help">How can I help you?</label>
            <input type="text" id="help" value="Enter your question here" name='whatever'>
            <button type="submit" placeholder="send">Submit</button>
            <!-- <input type="submit" placeholder="send"> -->
        </form>

        <p>It was long and hard but finally the basic chat is here.</p>

        <nav>
            <a href="/">Back to the first page</a>
        </nav>
    </body>
