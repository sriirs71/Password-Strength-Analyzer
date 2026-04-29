const pwd = document.getElementById("password");
const meterBar = document.getElementById("meterBar");
const meterText = document.getElementById("meterText");
const toggle = document.getElementById("togglePassword");
const themeBtn = document.getElementById("themeToggle");

if (pwd){
pwd.addEventListener("input", () => {
    const val = pwd.value;
    let score = 0;

    if (val.length >= 8) score++;
    if (/[A-Z]/.test(val)) score++;
    if (/[a-z]/.test(val)) score++;
    if (/[0-9]/.test(val)) score++;
    if (/[!@#$%^&*]/.test(val)) score++;

    const percent = (score / 5) * 100;
    meterBar.style.width = percent + "%";

    if (score <= 2){
        meterBar.style.background = "#e74c3c";
        meterText.innerText = "Weak Password";
    } else if (score <= 4){
        meterBar.style.background = "#f39c12";
        meterText.innerText = "Moderate Password";
    } else {
        meterBar.style.background = "#27ae60";
        meterText.innerText = "Strong Password";
    }
});
}

// Show / Hide password
if (toggle){
toggle.addEventListener("click", () => {
    pwd.type = pwd.type === "password" ? "text" : "password";
});
}

// Copy suggested password
const copyBtn = document.getElementById("copyBtn");
if (copyBtn){
copyBtn.addEventListener("click", () => {
    const text = document.getElementById("suggestedPwd").innerText;
    navigator.clipboard.writeText(text);
    copyBtn.innerText = "Copied!";
});
}

// Dark / Light theme
themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
});