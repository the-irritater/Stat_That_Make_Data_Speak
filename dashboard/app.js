// ===== Data Configuration =====
const DAYS = [
    { day: 31, topic: "What is a Dataset?" },
    { day: 32, topic: "Structured vs Unstructured Data" },
    { day: 33, topic: "Primary vs Secondary Data" },
    { day: 34, topic: "Cross-Sectional vs Time Series Data" },
    { day: 35, topic: "Clean Data vs Messy Data" },
    { day: 36, topic: "Missing Values" },
    { day: 37, topic: "Outlier Detection" },
    { day: 38, topic: "Data Cleaning" },
    { day: 39, topic: "Data Transformation" },
    { day: 40, topic: "Exploratory Data Analysis" },
    { day: 41, topic: "Frequency Table" },
    { day: 42, topic: "Cross-Tabulation" },
    { day: 43, topic: "Bar Chart vs Histogram" },
    { day: 44, topic: "Box Plot" },
    { day: 45, topic: "Scatter Plot" },
    { day: 46, topic: "Correlation Matrix" },
    { day: 47, topic: "Simpson's Paradox" },
    { day: 48, topic: "Confounding Variable" },
    { day: 49, topic: "Bias in Data" },
    { day: 50, topic: "Sampling Bias" },
    { day: 51, topic: "Response Bias" },
    { day: 52, topic: "Margin of Error" },
    { day: 53, topic: "Statistical vs Practical Significance" },
    { day: 54, topic: "Effect Size" },
    { day: 55, topic: "Assumptions in Statistics" },
    { day: 56, topic: "Normality Assumption" },
    { day: 57, topic: "Homogeneity of Variance" },
    { day: 58, topic: "Multicollinearity" },
    { day: 59, topic: "Residuals in Regression" },
    { day: 60, topic: "Practical Statistics Recap" }
];

const WEEKS = [
    { week: 1, goal: "Create repo and finish 2 applied notebooks", output: "1 signature post" },
    { week: 2, goal: "Finish first module and one case study", output: "1 full case study post" },
    { week: 3, goal: "Build one strong EDA notebook and one mini analysis", output: "1 insight post" },
    { week: 4, goal: "Add hypothesis testing or correlation project", output: "1 chart-led post" },
    { week: 5, goal: "Add regression-based analysis", output: "1 decision-focused post" },
    { week: 6, goal: "Create second full case study", output: "1 case study post" },
    { week: 7, goal: "Add business analytics or A/B testing project", output: "1 high-effort post" },
    { week: 8, goal: "Clean GitHub, pin best posts, improve README", output: "1 portfolio summary post" }
];

const CHECK_LABELS = ["Caption", "Template", "Visual", "Posted", "GitHub"];

// ===== Local Storage =====
const STORAGE_KEY = "stats_dashboard_v2";

function loadState() {
    try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) return JSON.parse(saved);
    } catch (e) {}
    return getDefaultState();
}

function saveState(state) {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {}
}

function getDefaultState() {
    return {
        weeks: WEEKS.map(() => false),
        days: DAYS.map(() => CHECK_LABELS.map(() => false)),
        notebooks: 0,
        casestudies: 0
    };
}

let state = loadState();

// ===== Render Timeline =====
function renderTimeline() {
    const container = document.getElementById("timeline");
    container.innerHTML = "";

    WEEKS.forEach((w, i) => {
        const div = document.createElement("div");
        div.className = `timeline-week${state.weeks[i] ? " completed" : ""}`;
        div.innerHTML = `
            <label class="week-label" style="display:flex;align-items:center;gap:10px;cursor:pointer;">
                <input type="checkbox" class="week-checkbox" data-week="${i}" ${state.weeks[i] ? "checked" : ""}>
                Week ${w.week}
            </label>
            <span class="week-goal">${w.goal}</span>
            <span class="week-output">${w.output}</span>
        `;
        container.appendChild(div);
    });

    container.addEventListener("change", (e) => {
        if (e.target.classList.contains("week-checkbox")) {
            const idx = parseInt(e.target.dataset.week);
            state.weeks[idx] = e.target.checked;
            saveState(state);
            renderTimeline();
            updateProgress();
        }
    });
}

// ===== Render Checklist =====
function renderChecklist(filter = "all") {
    const container = document.getElementById("checklistGrid");
    container.innerHTML = "";

    DAYS.forEach((d, dayIdx) => {
        const allDone = state.days[dayIdx].every(Boolean);
        const anyDone = state.days[dayIdx].some(Boolean);

        if (filter === "done" && !allDone) return;
        if (filter === "pending" && allDone) return;

        const item = document.createElement("div");
        item.className = `checklist-item${allDone ? " done" : ""}`;
        item.innerHTML = `
            <span class="day-number">Day ${d.day}</span>
            <span class="day-topic">${d.topic}</span>
            <div class="checklist-checks">
                ${CHECK_LABELS.map((label, checkIdx) => `
                    <input type="checkbox" class="mini-check" 
                        title="${label}" 
                        data-day="${dayIdx}" 
                        data-check="${checkIdx}"
                        ${state.days[dayIdx][checkIdx] ? "checked" : ""}>
                `).join("")}
            </div>
        `;
        container.appendChild(item);
    });

    container.addEventListener("change", (e) => {
        if (e.target.classList.contains("mini-check")) {
            const dayIdx = parseInt(e.target.dataset.day);
            const checkIdx = parseInt(e.target.dataset.check);
            state.days[dayIdx][checkIdx] = e.target.checked;
            saveState(state);
            updateProgress();
            // Update done class
            const allDone = state.days[dayIdx].every(Boolean);
            e.target.closest(".checklist-item").classList.toggle("done", allDone);
        }
    });
}

// ===== Filter Buttons =====
document.querySelectorAll(".filter-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        renderChecklist(btn.dataset.filter);
    });
});

// ===== Progress Rings =====
function setRingProgress(ringId, current, max) {
    const ring = document.getElementById(ringId);
    if (!ring) return;
    const circumference = 2 * Math.PI * 52;
    const progress = max > 0 ? current / max : 0;
    const offset = circumference * (1 - progress);
    ring.style.strokeDasharray = circumference;
    ring.style.strokeDashoffset = offset;
}

function updateProgress() {
    // Count fully completed days (all 5 checks)
    const postsPosted = state.days.filter(d => d[3]).length; // "Posted" checkbox
    const visualsDone = state.days.filter(d => d[2]).length; // "Visual" checkbox
    
    document.getElementById("postsCount").textContent = `${postsPosted}/30`;
    document.getElementById("visualsCount").textContent = `${visualsDone}/30`;
    document.getElementById("notebooksCount").textContent = `${state.notebooks}/10`;
    document.getElementById("casestudiesCount").textContent = `${state.casestudies}/3`;

    setRingProgress("postsRing", postsPosted, 30);
    setRingProgress("visualsRing", visualsDone, 30);
    setRingProgress("notebooksRing", state.notebooks, 10);
    setRingProgress("casestudiesRing", state.casestudies, 3);

    // Overall progress
    const totalChecks = state.days.flat().filter(Boolean).length;
    const maxChecks = DAYS.length * CHECK_LABELS.length;
    const weeksDone = state.weeks.filter(Boolean).length;
    const overallPct = Math.round(((totalChecks / maxChecks) * 0.7 + (weeksDone / WEEKS.length) * 0.3) * 100);
    document.getElementById("overallProgress").querySelector(".stat-value").textContent = `${overallPct}%`;
}

// ===== Notebook & Case Study Counters =====
// Make progress cards clickable for notebooks and case studies
document.querySelectorAll(".progress-card").forEach(card => {
    const type = card.dataset.type;
    if (type === "notebooks" || type === "casestudies") {
        card.style.cursor = "pointer";
        card.addEventListener("click", (e) => {
            if (e.target.classList.contains("mini-check") || e.target.classList.contains("week-checkbox")) return;
            const max = type === "notebooks" ? 10 : 3;
            state[type] = (state[type] + 1) % (max + 1);
            saveState(state);
            updateProgress();
        });
        card.title = "Click to increment";
    }
});

// ===== Insight Quality Checker =====
document.getElementById("checkInsightBtn").addEventListener("click", () => {
    const text = document.getElementById("insightInput").value.trim();
    if (!text) return;

    const results = [];
    
    // Check for numbers
    const hasNumber = /\d+(\.\d+)?(%|×|x|\s*(percent|lakh|crore|thousand|million|billion|hours?|days?|months?|years?|times|rupees?))/i.test(text) 
                   || /\d{2,}/.test(text) 
                   || /₹/.test(text);
    results.push({
        pass: hasNumber,
        label: "Contains a specific number or measurement"
    });

    // Check for comparison
    const hasComparison = /(higher|lower|more|less|greater|fewer|increase|decrease|compared|versus|vs\.?|than|but|however|while|although|whereas|difference|gap|contrast|×|x\s*more)/i.test(text);
    results.push({
        pass: hasComparison,
        label: "Contains a comparison (higher/lower, more/less, vs)"
    });

    // Check for surprise or caveat
    const hasSurprise = /(surprising|unexpected|contrary|despite|interestingly|notably|remarkably|however|but|although|yet|still|nonetheless|even though|paradox|counter|reverse|not|no significant|insignificant|caveat|limitation|risk|warning|caution|suggests|implies|may not|does not|didn't|doesn't)/i.test(text);
    results.push({
        pass: hasSurprise,
        label: "Contains a surprise, caveat, or nuance"
    });

    // Check length
    const wordCount = text.split(/\s+/).length;
    const goodLength = wordCount >= 15 && wordCount <= 60;
    results.push({
        pass: goodLength,
        label: `Good length (${wordCount} words — aim for 15–60)`
    });

    // Check for decision relevance
    const hasDecision = /(decision|recommend|suggest|action|should|strategy|implies|means|therefore|invest|focus|prioritize|allocate|target|risk|avoid|prevent|support|improve|optimize)/i.test(text);
    results.push({
        pass: hasDecision,
        label: "Supports a decision or action"
    });

    const passCount = results.filter(r => r.pass).length;
    
    const resultsDiv = document.getElementById("insightResults");
    resultsDiv.innerHTML = results.map(r => `
        <div class="result-item">
            <span class="result-icon ${r.pass ? "pass" : "fail"}">${r.pass ? "✓" : "✗"}</span>
            <span>${r.label}</span>
        </div>
    `).join("");

    let gradeClass, gradeText;
    if (passCount >= 4) {
        gradeClass = "grade-strong";
        gradeText = `Strong insight (${passCount}/5) — Ready to post!`;
    } else if (passCount >= 2) {
        gradeClass = "grade-ok";
        gradeText = `Decent insight (${passCount}/5) — Can be improved with more specifics.`;
    } else {
        gradeClass = "grade-weak";
        gradeText = `Weak insight (${passCount}/5) — Add a number, comparison, or surprise.`;
    }

    resultsDiv.innerHTML += `<div class="result-grade ${gradeClass}">${gradeText}</div>`;
    resultsDiv.classList.add("visible");
});

// ===== Reset =====
document.getElementById("resetBtn").addEventListener("click", () => {
    if (confirm("Reset all progress? This cannot be undone.")) {
        state = getDefaultState();
        saveState(state);
        renderTimeline();
        renderChecklist();
        updateProgress();
    }
});

// ===== Initialize =====
renderTimeline();
renderChecklist();
updateProgress();

// Animate rings on load
setTimeout(() => {
    updateProgress();
}, 100);
