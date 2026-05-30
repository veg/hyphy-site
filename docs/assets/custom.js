document.addEventListener("DOMContentLoaded", function() {
    // 1. Add version number to top right of navbar (clock style)
    var navs = document.querySelectorAll("ul.navbar-nav.ml-auto");
    if (navs.length > 0) {
        var versionLi = document.createElement("li");
        versionLi.className = "nav-item hyphy-version-clock";
        var versionLink = document.createElement("a");
        versionLink.href = "https://github.com/veg/hyphy/releases";
        versionLink.target = "_blank";
        versionLink.className = "nav-link";
        versionLink.textContent = window.HYPHY_VERSION || "v2.5.62";
        versionLi.appendChild(versionLink);
        navs[0].appendChild(versionLi);
    }

    // 2. Add GitHub link to left-hand sidebar navigation on the home page
    var homeHeading = document.getElementById("hypothesis-testing-using-phylogenies-hyphy");
    if (homeHeading) {
        var sidebarNav = document.querySelector(".bs-sidebar .nav.flex-column");
        if (sidebarNav) {
            var githubLi = document.createElement("li");
            githubLi.className = "nav-item github-sidebar-link";
            githubLi.style.marginTop = "15px";
            githubLi.style.borderTop = "1px dashed #000000";
            githubLi.style.paddingTop = "10px";
            
            var githubLink = document.createElement("a");
            githubLink.href = "https://github.com/veg/hyphy";
            githubLink.target = "_blank";
            githubLink.className = "nav-link";
            githubLink.style.fontWeight = "bold";
            githubLink.style.display = "flex";
            githubLink.style.alignItems = "center";
            githubLink.style.gap = "6px";
            
            githubLink.innerHTML = '<i class="fa fa-github" style="margin-right: 6px; font-size: 14px;"></i> HyPhy on GitHub';
            
            githubLi.appendChild(githubLink);
            sidebarNav.appendChild(githubLi);
        }
    }
});
