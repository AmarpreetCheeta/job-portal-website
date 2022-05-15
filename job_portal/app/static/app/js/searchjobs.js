/*let r = windows.location.search;
if(ijob!=null)
{
    const search = () => {
        const searchbox = document.getElementsByName("sjob").value.toUpperCase
        const storeitems = document.getElementById("jobs-list")
        const jobs = document.querySelectorAll(".jobs")
        const jname = document.getElementsByTagName("h2")

        for (var i = 0; i < jname.length; i++) {
            let match = jobs[i].getElementsByTagName('h2')[0];

            if (match) {
                let textvalue = match.textContent || match.innerHTML

                if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
                    jobs[i].style.display = "";
                }
                else {
                    jobs[i].style.display = "none";
                }
            }
        }
    }
}
else*/

const search = () => {
    const searchbox = document.getElementById("search-item").value.toUpperCase();
    const storeitems = document.getElementById("jobs-list")
    const jobs = document.querySelectorAll(".jobs")
    const jname = document.querySelectorAll("._types")

    for (var i = 0; i < jname.length; i++) {
        let match = jobs[i].querySelectorAll('._types')[0];

        if (match) {
            let textvalue = match.textContent || match.innerHTML

            if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
                jobs[i].style.display = "";
            }
            else {
                jobs[i].style.display = "none";
                document.getElementById("_no_").style.display = "block"
            }
        }
    }
}
