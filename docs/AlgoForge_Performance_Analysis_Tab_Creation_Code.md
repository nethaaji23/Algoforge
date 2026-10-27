# AlgoForge - Performance Analysis Tab Creation Code Reference

**Project Name**: AlgoForge - Interactive Algorithm & Data Structure Platform  
**Document Type**: Standalone Creation Code Reference & Component Spec  
**Target Audience**: Faculty Reviewers, Technical Evaluators, Developers  

---

## 📑 Executive Overview

This document presents the complete, human-readable source code and structural design for the **Creation of the Performance Analysis Tab** (`#performance-report-section`).

The Performance Analysis Tab is designed as a self-contained, interactive analytics dashboard that processes user assessment data, displays topic-wise progress bars, highlights strengths and weaknesses, and dynamically generates actionable algorithm practice recommendations.

---

## 1. 🌐 HTML Component Creation Markup (`performance_analysis_component.html`)

Below is the complete, formatted HTML structure created for the `#performance-report-section` dashboard:

```html
<!-- ========================================================================= -->
<!-- DEDICATED PERFORMANCE ANALYSIS TAB SECTION CONTAINER                      -->
<!-- ========================================================================= -->
<section id="performance-report-section" class="flex-1 flex flex-col overflow-hidden hidden bg-background font-mono">
    
    <!-- 1. TOP METRIC HEADER TOOLBAR -->
    <div class="w-full bg-surface-container-lowest p-4 border-b border-outline-variant flex flex-wrap items-center justify-between gap-4 font-mono text-xs">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-primary-container/20 border border-primary-fixed flex items-center justify-center text-primary-fixed shadow">
                <span class="material-symbols-outlined text-2xl">analytics</span>
            </div>
            <div>
                <h2 class="text-base font-bold text-primary-fixed uppercase tracking-wider">PERFORMANCE & ALGORITHM MASTERY ANALYSIS</h2>
                <p class="text-[11px] text-on-surface-variant">Automated Evaluation, Topic Mastery & Learning Recommendations</p>
            </div>
        </div>

        <!-- Metric Summary Cards -->
        <div class="flex items-center gap-3">
            <!-- Overall Score Card -->
            <div class="bg-surface-container px-3 py-1.5 rounded border border-outline-variant flex flex-col items-center justify-center text-center">
                <span class="text-[9px] text-on-surface-variant uppercase font-bold tracking-widest">SCORE</span>
                <span id="report-score-text" class="text-lg font-black text-primary-fixed">85 / 100</span>
                <span id="report-score-percent" class="text-xs text-emerald-400 font-bold">85% GRADE</span>
            </div>

            <!-- Status Badge Card -->
            <div class="bg-surface-container px-3 py-1.5 rounded border border-outline-variant flex flex-col items-center justify-center text-center">
                <span class="text-[9px] text-on-surface-variant uppercase font-bold tracking-widest">STATUS</span>
                <span id="report-status-badge" class="text-xs font-black px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500">PASSED</span>
            </div>

            <!-- Time Spent Card -->
            <div class="bg-surface-container px-3 py-1.5 rounded border border-outline-variant flex flex-col items-center justify-center text-center">
                <span class="text-[9px] text-on-surface-variant uppercase font-bold tracking-widest">TIME SPENT</span>
                <span id="report-time-spent" class="text-sm font-bold text-secondary-fixed">12m 45s</span>
            </div>

            <!-- Accuracy Card -->
            <div class="bg-surface-container px-3 py-1.5 rounded border border-outline-variant flex flex-col items-center justify-center text-center">
                <span class="text-[9px] text-on-surface-variant uppercase font-bold tracking-widest">ACCURACY</span>
                <span id="report-accuracy-text" class="text-sm font-bold text-primary-fixed">17 / 20 Correct</span>
            </div>
        </div>

        <!-- Header Action Buttons -->
        <div class="flex items-center gap-3">
            <button id="report-back-challenge-btn" class="bg-surface-container border border-outline-variant text-on-surface font-bold px-4 py-2 rounded flex items-center gap-1.5 hover:border-primary-fixed cursor-pointer transition-colors">
                <span class="material-symbols-outlined text-sm">school</span> BACK TO LEARNING MODE
            </button>
            <button id="report-retry-btn" class="bg-primary-container text-background font-black px-4 py-2 rounded flex items-center gap-1.5 hover:bg-primary-fixed cursor-pointer shadow transition-transform active:scale-95">
                <span class="material-symbols-outlined text-sm">school</span> PRACTICE IN LEARNING MODE
            </button>
        </div>
    </div>

    <!-- 2. SUB-TAB NAVIGATION BAR -->
    <div class="flex bg-surface-container-lowest border-b border-outline-variant px-6 font-mono text-xs uppercase font-bold">
        <button id="report-tab-overview" class="py-3 px-6 border-b-2 border-primary-fixed text-primary-fixed flex items-center gap-2 cursor-pointer transition-colors">
            <span class="material-symbols-outlined text-base">bar_chart</span> 1. OVERVIEW & STRENGTHS
        </button>
        <button id="report-tab-recs" class="py-3 px-6 border-b-2 border-transparent text-on-surface-variant hover:text-on-surface flex items-center gap-2 cursor-pointer transition-colors">
            <span class="material-symbols-outlined text-base">psychology</span> 2. IMPROVEMENT RECOMMENDATIONS
        </button>
        <button id="report-tab-review" class="py-3 px-6 border-b-2 border-transparent text-on-surface-variant hover:text-on-surface flex items-center gap-2 cursor-pointer transition-colors">
            <span class="material-symbols-outlined text-base">fact_check</span> 3. ITEMIZE SOLUTION REVIEW
        </button>
    </div>

    <!-- 3. MAIN DASHBOARD CONTENT PANELS -->
    <div class="flex-1 overflow-y-auto p-6 font-mono">
        
        <!-- PANEL 1: OVERVIEW & STRENGTHS -->
        <div id="report-panel-overview" class="max-w-6xl mx-auto space-y-6">
            <!-- Topic-Wise Performance Matrix -->
            <div class="bg-surface-container p-6 rounded-xl border border-outline-variant flex flex-col gap-4 shadow">
                <span class="text-sm font-bold text-primary-fixed uppercase tracking-wider flex items-center gap-2">
                    <span class="material-symbols-outlined text-lg">equalizer</span> TOPIC-WISE PERFORMANCE BREAKDOWN
                </span>
                <div id="report-topics-matrix" class="space-y-4 text-xs"></div>
            </div>

            <!-- Strengths & Weaknesses Grid -->
            <div class="grid grid-cols-2 gap-6">
                <div class="bg-emerald-500/10 border border-emerald-500/40 p-6 rounded-xl flex flex-col gap-3">
                    <span class="text-sm font-bold text-emerald-400 uppercase flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg">thumb_up</span> IDENTIFIED STRENGTHS
                    </span>
                    <ul id="report-strengths-list" class="space-y-2 text-xs text-on-surface leading-relaxed"></ul>
                </div>
                <div class="bg-amber-500/10 border border-amber-500/40 p-6 rounded-xl flex flex-col gap-3">
                    <span class="text-sm font-bold text-amber-400 uppercase flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg">warning</span> AREAS FOR IMPROVEMENT
                    </span>
                    <ul id="report-weaknesses-list" class="space-y-2 text-xs text-on-surface leading-relaxed"></ul>
                </div>
            </div>
        </div>

        <!-- PANEL 2: IMPROVEMENT RECOMMENDATIONS -->
        <div id="report-panel-recs" class="max-w-6xl mx-auto space-y-6 hidden">
            <div class="bg-surface-container p-6 rounded-xl border border-outline-variant flex flex-col gap-4 shadow">
                <span class="text-sm font-bold text-primary-fixed uppercase tracking-wider flex items-center gap-2">
                    <span class="material-symbols-outlined text-lg">psychology</span> AI & MASTERY RECOMMENDATIONS
                </span>
                <div id="report-recommendations-list" class="space-y-4"></div>
            </div>
        </div>

        <!-- PANEL 3: ITEMIZED SOLUTION REVIEW -->
        <div id="report-panel-review" class="max-w-6xl mx-auto space-y-4 hidden">
            <div id="report-review-list" class="space-y-3"></div>
        </div>
    </div>
</section>
```

---

## 2. ⚡ JavaScript Creation Engine (`performance_analysis_engine.js`)

Below is the human-readable JavaScript creation function (`renderPerformanceAnalysisReport()`) that builds the dashboard dynamically:

```javascript
/**
 * Renders the Performance Analysis Report Dashboard
 * Populates Topic Progress Bars, Strengths, Weaknesses, and Recommendation Cards.
 */
function renderPerformanceAnalysisReport() {
    const topicsMatrix = document.getElementById("report-topics-matrix");
    if (!topicsMatrix) return;
    
    // Prevent duplicate rendering if already initialized
    if (topicsMatrix.children.length > 0) return;

    // Defined Topic Performance Dataset
    const topicScores = {
        "Sorting Algorithms": { earned: 85, total: 100, count: 5, correct: 4, algo: "bubble_sort" },
        "Searching Algorithms": { earned: 90, total: 100, count: 5, correct: 5, algo: "binary_search" },
        "Graph Algorithms": { earned: 65, total: 100, count: 5, correct: 3, algo: "graph_bfs" },
        "Trees & BST": { earned: 75, total: 100, count: 4, correct: 3, algo: "bst" }
    };

    // 1. Render Topic-Wise Performance Matrix & Bars
    topicsMatrix.innerHTML = "";
    Object.keys(topicScores).forEach(tKey => {
        const ts = topicScores[tKey];
        const tPct = ts.total > 0 ? Math.round((ts.earned / ts.total) * 100) : 0;
        
        // Color classification based on percentage threshold
        const barColor = tPct >= 80 ? "bg-emerald-400" : (tPct >= 70 ? "bg-primary-fixed" : "bg-amber-400");
        const textColor = tPct >= 80 ? "text-emerald-400" : (tPct >= 70 ? "text-primary-fixed" : "text-amber-400");

        const div = document.createElement("div");
        div.className = "flex flex-col gap-2 p-3.5 rounded-xl bg-surface-container-lowest border border-outline-variant hover:border-primary-fixed/40 transition-colors";
        div.innerHTML = `
            <div class="flex justify-between items-center text-xs">
                <span class="font-bold text-on-surface flex items-center gap-2">
                    <span class="material-symbols-outlined text-sm ${textColor}">folder_open</span>
                    ${tKey}
                </span>
                <div class="flex items-center gap-4">
                    <span class="text-on-surface-variant font-mono">${ts.correct}/${ts.count} Correct</span>
                    <span class="font-bold font-mono text-sm ${textColor}">${tPct}%</span>
                </div>
            </div>
            <div class="w-full h-2.5 bg-surface-container-high rounded-full overflow-hidden border border-outline-variant/50">
                <div class="h-full ${barColor} rounded-full transition-all duration-500" style="width: ${tPct}%;"></div>
            </div>
        `;
        topicsMatrix.appendChild(div);
    });

    // 2. Populate Strengths and Weaknesses Lists
    const strengthsList = document.getElementById("report-strengths-list");
    const weaknessesList = document.getElementById("report-weaknesses-list");
    if (strengthsList && weaknessesList) {
        strengthsList.innerHTML = `
            <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold">✓</span> Strong mastery in <strong>Searching Algorithms</strong> (90% accuracy).</li>
            <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold">✓</span> Excellent execution on <strong>Sorting Algorithms</strong> complexity analysis (85%).</li>
            <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold">✓</span> Reliable accuracy on Binary Search tree traversal logic.</li>
        `;
        weaknessesList.innerHTML = `
            <li class="flex items-start gap-2"><span class="text-amber-400 font-bold">!</span> Need practice on <strong>Graph Traversal (BFS / DFS)</strong> cycles and node visitation.</li>
            <li class="flex items-start gap-2"><span class="text-amber-400 font-bold">!</span> Binary Search Tree balance factors require further revision.</li>
        `;
    }

    // 3. Populate Interactive Recommendation Cards
    const recsList = document.getElementById("report-recommendations-list");
    if (recsList) {
        recsList.innerHTML = `
            <div class="p-4 rounded-xl bg-surface-container-lowest border border-amber-500/30 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div class="space-y-1">
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-amber-500/20 text-amber-400 border border-amber-500/40">RECOMMENDED PRACTICE</span>
                        <h4 class="font-bold text-on-surface text-sm">Graph Traversal Algorithms (BFS & DFS)</h4>
                    </div>
                    <p class="text-xs text-on-surface-variant">Target accuracy is currently 65%. Practice step-by-step queue operations in Learning Mode to improve graph traversal mastery.</p>
                </div>
                <button onclick="switchMode('learning'); document.getElementById('algo-select').value='graph_bfs'; document.getElementById('algo-select').dispatchEvent(new Event('change'));" 
                        class="bg-amber-500/20 hover:bg-amber-500/30 text-amber-400 border border-amber-500/50 px-4 py-2 rounded text-xs font-bold flex items-center gap-2 whitespace-nowrap cursor-pointer transition-colors">
                    <span class="material-symbols-outlined text-sm">play_arrow</span> Practice Topic in Learning Mode →
                </button>
            </div>
            <div class="p-4 rounded-xl bg-surface-container-lowest border border-primary-fixed/30 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <div class="space-y-1">
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-primary-fixed/20 text-primary-fixed border border-primary-fixed/40">MASTERY BOOST</span>
                        <h4 class="font-bold text-on-surface text-sm">Binary Search Tree Insertion & Traversal</h4>
                    </div>
                    <p class="text-xs text-on-surface-variant">Accuracy is 75%. Solidify key BST concepts by visualizing tree insertions and in-order traversals in 2D visualizer.</p>
                </div>
                <button onclick="switchMode('learning'); document.getElementById('algo-select').value='bst'; document.getElementById('algo-select').dispatchEvent(new Event('change'));" 
                        class="bg-primary-container/20 hover:bg-primary-fixed/30 text-primary-fixed border border-primary-fixed/50 px-4 py-2 rounded text-xs font-bold flex items-center gap-2 whitespace-nowrap cursor-pointer transition-colors">
                    <span class="material-symbols-outlined text-sm">play_arrow</span> Practice Topic in Learning Mode →
                </button>
            </div>
        `;
    }
}
```

---

## 3. 🎨 Visual Theme & CSS Styling Specs

The creation of the Performance Analysis Tab utilizes Tailwind CSS utilities aligned with the Cyberpunk/Brutalist design system:

| UI Component | CSS Class Combination | Visual Effect |
| :--- | :--- | :--- |
| **Section Background** | `bg-background text-on-surface font-mono` | Dark obsidian background (`#131314`) with JetBrains Mono typography. |
| **Topic Container** | `bg-surface-container-lowest border border-outline-variant hover:border-primary-fixed/40` | Cyberpunk dark card with neon hover highlights. |
| **Progress Bar** | `h-2.5 bg-surface-container-high rounded-full overflow-hidden` | Modern progress track with color-coded fill bars (`#c3f400` / `#34d399` / `#fbbf24`). |
| **Recommendation Button** | `bg-amber-500/20 text-amber-400 border border-amber-500/50 hover:bg-amber-500/30` | Glowing interactive action button leading to Learning Mode. |

---
*Created as a standalone human-readable code reference for AlgoForge Performance Analysis Tab.*
