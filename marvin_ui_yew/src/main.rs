use yew::prelude::*;

#[function_component]
fn App() -> Html {
    let counter = use_state(|| 0);
    let onclick = {
        let counter = counter.clone();
        // move |_| {
        //     let value = *counter + 1;
        //     counter.set(value);
        // }
    };

    html! {
        <>
        <div class="navbar bg-base-300">
            <div class="flex-1">
                <div class="normal-case text-xl">{"FarPI - Yew"}</div>
            </div>
            <div class="flex-none">
                <div class="tabs tabs-boxed">
                    <a class="tab tab-lg">{"Tab 1"}</a>
                    <a class="tab tab-lg tab-active">{"Tab 2"}</a>
                    <a class="tab tab-lg">{"Tab 3"}</a>
                </div>
            </div>
        </div>
        {"Content Goes Here"}
        </>
    }
}

fn main() {
    yew::Renderer::<App>::new().render();
}
