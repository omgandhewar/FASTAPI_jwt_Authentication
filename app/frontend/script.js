const API = "http://127.0.0.1:8000";

// ================= TABS =================

const loginTab = document.getElementById("loginTab");
const signupTab = document.getElementById("signupTab");

const loginForm = document.getElementById("loginForm");
const signupCard = document.getElementById("signupCard");

loginTab.onclick = () => {

    loginTab.classList.add("active");
    signupTab.classList.remove("active");

    loginForm.parentElement.classList.remove("hidden");
    signupCard.classList.add("hidden");

};

signupTab.onclick = () => {

    signupTab.classList.add("active");
    loginTab.classList.remove("active");

    signupCard.classList.remove("hidden");
    loginForm.parentElement.classList.add("hidden");

};

// ================= LOGIN =================

loginForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const email = document.getElementById("loginEmail").value;

    const password = document.getElementById("loginPassword").value;

    const response = await fetch(`${API}/login`, {

        method: "POST",

        credentials: "include",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            email,
            password
        })

    });

    const data = await response.json();

    alert(data.message);

});

// ================= SIGNUP =================

document.getElementById("signupForm")
.addEventListener("submit", async (e) => {

    e.preventDefault();

    const name = document.getElementById("signupName").value;

    const email = document.getElementById("signupEmail").value;

    const password = document.getElementById("signupPassword").value;

    const response = await fetch(`${API}/register`, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            name,
            email,
            password

        })

    });

    const data = await response.json();

    alert(data.message);

});

// ================= CURRENT USER =================

document.getElementById("currentUserBtn")
.addEventListener("click", async () => {

    const response = await fetch(`${API}/currentuser`, {

        method: "GET",

        credentials: "include"

    });

    const data = await response.json();

    document.getElementById("userId").innerText =
        data.id ?? "-";

    document.getElementById("userName").innerText =
        data.name ?? "-";

    document.getElementById("userEmail").innerText =
        data.email ?? "-";

    document.getElementById("protectedResponse")
        .innerText =
        JSON.stringify(data, null, 4);

});

// ================= LOGOUT =================

document.getElementById("logoutBtn")
.addEventListener("click", async () => {

    const response = await fetch(`${API}/logout`, {

        method: "POST",

        credentials: "include"

    });

    const data = await response.json();

    alert(data.message);

    document.getElementById("userId").innerText = "-";
    document.getElementById("userName").innerText = "-";
    document.getElementById("userEmail").innerText = "-";

    document.getElementById("payload").innerText = "";

    document.getElementById("protectedResponse").innerText = "";

});

// ================= SHOW JWT PAYLOAD =================

document.getElementById("payloadBtn")
.addEventListener("click", async () => {

    const response = await fetch(`${API}/payload`, {

        method: "GET",

        credentials: "include"

    });

    const data = await response.json();

    document.getElementById("payload").innerText =
        JSON.stringify(data, null, 4);

});

// ================= REFRESH TOKEN =================

async function refreshToken() {

    const response = await fetch(`${API}/refresh`, {

        method: "POST",

        credentials: "include"

    });

    const data = await response.json();

    alert(data.message);

}

// ================= GET PROTECTED ROUTE =================

async function protectedRoute() {

    const response = await fetch(`${API}/protected`, {

        method: "GET",

        credentials: "include"

    });

    const data = await response.json();

    document.getElementById("protectedResponse")
        .innerText =
        JSON.stringify(data, null, 4);

}

// ================= SHOW ACCESS TOKEN =================

async function showAccessToken() {

    const response = await fetch(`${API}/access-token`, {

        credentials: "include"

    });

    const data = await response.json();

    document.getElementById("accessToken").value =
        data.access_token || "";

}

// ================= SHOW REFRESH TOKEN =================

async function showRefreshToken() {

    const response = await fetch(`${API}/refresh-token`, {

        credentials: "include"

    });

    const data = await response.json();

    document.getElementById("refreshToken").value =
        data.refresh_token || "";

}

// ================= LOAD USER AFTER LOGIN =================

async function loadDashboard() {

    await protectedRoute();

    await showAccessToken();

    await showRefreshToken();

}

// ================= LOGIN UPDATE =================

// Replace this inside login success:

// if(response.ok){
//     loadDashboard();
// }

// ================= PAGE LOAD =================

window.onload = async () => {

    try{

        await protectedRoute();

    }
    catch(e){

        console.log("Not Logged In");

    }

};