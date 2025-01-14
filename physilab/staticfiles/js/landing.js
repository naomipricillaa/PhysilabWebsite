function handleScrollToSection(event) {
    event.preventDefault();
    scrollToCoursesSection();
}

function scrollToCoursesSection() {
    const coursesSection = document.querySelector('#courses-section');

    if (coursesSection) {
        coursesSection.scrollIntoView({
            behavior: 'smooth'
        });
    }
}

document.querySelector('.cta-btn').addEventListener('click', handleScrollToSection);