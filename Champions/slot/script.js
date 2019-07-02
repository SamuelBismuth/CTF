
let array = new Array();

for (let ind = 0; ind < 38; ind++) {
	array[ind] = new Set();
}

let goTo = 0;

for (let ehud = 0; ehud < 500; ehud++) {
	$.get('spin',{'coins':0}, function(data) {
		let result = data['result'];
		for (let at = 0; at < result.length; at++) {
			let char = result.charAt(at);
			array[at].add(char);
		}		
    }).then(()=>{
    	goTo++
		if (goTo == 499) {
			let str = ''
			for (let set of array) {
				for (let elem of set) {
					str += elem + ' '
				}
				str += "\n"
				
			}
		console.log(str);
		}
    });
}