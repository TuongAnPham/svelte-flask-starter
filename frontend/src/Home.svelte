<script>
	export let user;
</script>

<main>
	<h1>Hello {user}!</h1>
	
	<section class='section content'>
		<h2>I want to create a live chat that allows users to talk to the IT help desks</h2>
	</section>

	<section class='section content'>
		<h3>Desgin and Structure</h3>
		<p>It should look something like this:</p> 
		<!-- <img src="../frontend/src/chatbox.png" alt="Image of a service desk chat"> -->
		<p>My priority is to make the chatbox, but if there's still time after I've done it, designing the website to make it look better will be my second goal.</p>
	</section>

</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>