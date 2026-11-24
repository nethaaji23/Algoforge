# AlgoForge - Adding Performance Analysis Tab to Webpage Reference

**Project Name**: AlgoForge - Interactive Algorithm & Data Structure Platform  
**Document Type**: Standalone Integration & Wiring Manual  
**Target Audience**: Faculty Reviewers, Technical Evaluators, Web Developers  

---

## 📑 Executive Overview

This document provides a human-readable, step-by-step guide explaining **how the Performance Analysis Tab was added and integrated into the AlgoForge webpage**.

The integration process involves two primary codebase locations:
1. **Frontend Markup (`frontend/index.html`)**: Updating top navigation bar and mounting the `#performance-report-section` container.
2. **Application Engine (`frontend/app.js`)**: Updating mode switching logic (`switchMode`), handling navbar click events (`setupModeNavigation`), and wiring recommendation buttons to route back into Learning Mode algorithms.

---

## 1. 🌐 Webpage HTML Modifications (`frontend/index.html`)

To add the Performance Analysis Tab to the webpage, two modifications were made to `index.html`:

### Step 1.1: Updating Top Header Navbar Links

The navigation bar was updated to display two main mode buttons (**Learning Mode** and **Performance Analysis**):

```html
<!-- ========================================================================= -->
<!-- HEADER NAVBAR: DUAL-MODE NAVIGATION                                       -->
<!-- Location: frontend/index.html (inside <header><nav>)                      -->
<!-- ========================================================================= -->
<nav class="flex items-center gap-1 h-16 font-mono text-xs uppercase tracking-wider">
    <!-- 1. Learning Mode Button -->
    <button id="nav-mode-learning" 
            class="h-full px-4 flex items-center gap-1.5 text-primary-fixed border-b-2 border-primary-fixed bg-surface-container font-bold cursor-pointer transition-colors">
        <span class="material-symbols-outlined text-base">school</span> Learning Mode
    </button>
    
    <!-- 2. Performance Analysis Button -->
    <button id="nav-mode-report" 
            class="h-full px-4 flex items-center gap-1.5 text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high cursor-pointer transition-colors">
        <span class="material-symbols-outlined text-base">analytics</span> Performance Analysis
    </button>
</nav>
```

### Step 1.2: Mounting the Section Container into `<main>`

The `#performance-report-section` component was inserted into the primary main layout wrapper:

```html
<!-- ========================================================================= -->
<!-- MAIN WORKSPACE LAYOUT WRAPPER                                             -->
<!-- Location: frontend/index.html (inside <main>)                             -->
<!-- ========================================================================= -->
<main class="flex-1 flex overflow-hidden relative">
    
    <!-- LEARNING MODE SECTION (VISUALIZER + TELEMETRY) -->
    <section id="learning-mode-section" class="flex-1 flex overflow-hidden">
        <!-- Visualizer canvas, code panel, and controls -->
    </section>

    <!-- PERFORMANCE ANALYSIS SECTION (NEWLY ADDED) -->
    <section id="performance-report-section" class="flex-1 flex flex-col overflow-hidden hidden bg-background font-mono">
        <!-- Header metrics, tabs, topic matrix, strengths/weaknesses, recommendations -->
    </section>
    
</main>
```

---

## 2. ⚡ JavaScript Engine Integration (`frontend/app.js`)

To enable seamless tab switching, performance calculations, and interactive recommendations, `app.js` was modified as follows:

### Step 2.1: View Routing & Tab State Management (`switchMode`)

The central mode switching function was updated to manage section visibility and active tab styling:

```javascript
/**
 * Global View Switching Engine
 * @param {string} mode - Active mode key ("learning" or "report")
 */
function switchMode(mode) {
    const navModeLearning = document.getElementById("nav-mode-learning");
    const navModeReport = document.getElementById("nav-mode-report");

    const sectionLearning = document.getElementById("learning-mode-section");
    const sectionReport = document.getElementById("performance-report-section");

    // Hide all sections by default
    if (sectionLearning) sectionLearning.classList.add("hidden");
    if (sectionReport) sectionReport.classList.add("hidden");

    // Reset default button styling (Inactive state)
    const inactiveClass = "h-full px-4 flex items-center gap-1.5 text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high cursor-pointer transition-colors";
    const activeClass = "h-full px-4 flex items-center gap-1.5 text-primary-fixed border-b-2 border-primary-fixed bg-surface-container font-bold cursor-pointer transition-colors";

    if (navModeLearning) navModeLearning.className = inactiveClass;
    if (navModeReport) navModeReport.className = inactiveClass;

    // Activate selected mode
    if (mode === "learning") {
        if (navModeLearning) navModeLearning.className = activeClass;
        if (sectionLearning) sectionLearning.classList.remove("hidden");
    } else if (mode === "report") {
        if (navModeReport) navModeReport.className = activeClass;
        if (sectionReport) sectionReport.classList.remove("hidden");
        
        // Execute dynamic report calculation and rendering
        renderPerformanceAnalysisReport();
    }
}
```

### Step 2.2: Event Listener Setup (`setupModeNavigation`)

Navbar buttons and performance action buttons were bound to execution listeners:

```javascript
/**
 * Binds click listeners for Navbar Mode Switching
 */
function setupModeNavigation() {
    const navModeLearning = document.getElementById("nav-mode-learning");
    const navModeReport = document.getElementById("nav-mode-report");

    if (navModeLearning) {
        navModeLearning.addEventListener("click", () => switchMode("learning"));
    }
    if (navModeReport) {
        navModeReport.addEventListener("click", () => switchMode("report"));
    }

    // Action buttons inside Performance Analysis header
    const reportBackBtn = document.getElementById("report-back-challenge-btn");
    const reportRetryBtn = document.getElementById("report-retry-btn");

    if (reportBackBtn) {
        reportBackBtn.addEventListener("click", () => switchMode("learning"));
    }
    if (reportRetryBtn) {
        reportRetryBtn.addEventListener("click", () => switchMode("learning"));
    }
}
```

### Step 2.3: Closed-Loop Recommendation Routing

When a user clicks on an improvement recommendation (e.g. `Practice Topic in Learning Mode →`), the event triggers:
1. `switchMode('learning')` - Changes the active screen view back to Learning Mode.
2. Selects the target algorithm in `#algo-select` (`bubble_sort`, `binary_search`, `graph_bfs`, `bst`).
3. Dispatches a `change` event to immediately trigger algorithm initialization and 2D canvas visualization.

```javascript
// Example Inline Event Handler generated by Recommendation Card
button.onclick = function() {
    switchMode('learning');
    const algoSelect = document.getElementById('algo-select');
    algoSelect.value = 'graph_bfs';
    algoSelect.dispatchEvent(new Event('change'));
};
```

---

## 3. 🧪 Runtime Verification & Testing Protocol

To verify that the Performance Analysis Tab was successfully added to the webpage:

1. **Start Local Backend Server**:
   ```bash
   python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
   ```
2. **Access Web Application**:
   Open browser at `http://127.0.0.1:8000/`.
3. **Navbar Verification**:
   Confirm header contains exactly 2 tabs: **Learning Mode** and **Performance Analysis**.
4. **Interactive Testing**:
   - Click **Performance Analysis** $\rightarrow$ verifies dynamic generation of score, progress bars, strengths/weaknesses, and recommendations.
   - Click **Practice Topic in Learning Mode →** $\rightarrow$ verifies smooth transition to Learning Mode with pre-selected algorithm loaded.

---
*Created as a standalone human-readable integration reference for AlgoForge Performance Analysis Tab.*
