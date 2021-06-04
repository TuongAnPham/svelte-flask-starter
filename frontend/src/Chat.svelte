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
        // input.value is the message text
        // http://127.0.0.1:8080/receive use this endpoint in place of "URL"
        axios.get('http://127.0.0.1:8080/receive', {params: {whatever: input.value} }).then(resp => {
            console.log("Sending message...")
            console.log(resp.data);
        })
    }

    setInterval(getdata, 1000);
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

        <nav>
            <a href="/about">Back to the first page</a>
        </nav>
    </body>

<style>
	header {
		color: #ff3e00;
        font-size: 1.5em;
		font-weight: 100;
	}
    /* div {
  background-color: lightgrey;
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
    } */
</style>