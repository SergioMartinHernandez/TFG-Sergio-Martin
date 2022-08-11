<template>
  <section>
    <div class="container align-items-center">
             <div class="row">
              <label id="label-history">Search History</label>
            </div>
      <div class="row">
             <li v-for="(item, index) in items">
        		{{ parentMessage }} - {{ index }} - {{ item.message }}
      </li>
            </div>
      
    </div>
  </section>
</template>

<script>
export default {
  data() {
  	return {
	    parentMessage: 'Parent',
    	items: [{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' },{ message: 'Foo' }, { message: 'Bar' }, { message: 'Foo' }, { message: 'Bar' }]
  	}
	}
}
</script>

<style>
  .container{
    margin-top: 3%;
    padding: 5em;
    background-color: aliceblue;
  }
  #label-history {
    margin-left: 16px;
    font-size: x-large;
    font-family: unset;
  }
</style>


